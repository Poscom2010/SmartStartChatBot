from langchain_community.vectorstores import FAISS

# Compatibility shim: some FAISS docstores were pickled with Pydantic v2 state
# (using 'fields_set') while the current runtime may deserialize via the
# pydantic.v1 BaseModel (expecting '__fields_set__'). We patch __setstate__ to
# accept either key so older/newer pickles load seamlessly.
try:
    from pydantic.v1.main import BaseModel as _PDBaseModel  # pydantic v2 shim path
except Exception:
    try:
        from pydantic.main import BaseModel as _PDBaseModel  # pydantic v1
    except Exception:
        _PDBaseModel = None  # If pydantic is unavailable, skip patching

if _PDBaseModel is not None:
    _orig_setstate = getattr(_PDBaseModel, "__setstate__", None)

    def _compat_setstate(self, state):
        if isinstance(state, dict):
            new_state = dict(state)
            if "__fields_set__" not in new_state:
                fields = new_state.pop("fields_set", None)
                new_state["__fields_set__"] = fields if fields is not None else set()
            if _orig_setstate is not None:
                return _orig_setstate(self, new_state)
            # Fallback: assign state directly if no original method
            for k, v in new_state.items():
                try:
                    setattr(self, k, v)
                except Exception:
                    pass
            return
        # Non-dict state: just forward to original if present, else ignore
        if _orig_setstate is not None:
            return _orig_setstate(self, state)

    try:
        _PDBaseModel.__setstate__ = _compat_setstate  # type: ignore[attr-defined]
    except Exception:
        pass

def load_vectorstore(embeddings):
    return FAISS.load_local(
        'smartstart_streamlit/smartstart_faiss_index',
        embeddings=embeddings,
        allow_dangerous_deserialization=True
    )
