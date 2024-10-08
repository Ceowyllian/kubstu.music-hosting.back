from functools import wraps

__all__ = [
    "with_likes",
]


def with_likes(target_type):
    @wraps
    def decorator(model_class):
        model_class.like_target_type = target_type
        return model_class

    return decorator
