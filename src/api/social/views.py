from api.common import GenericViewSet, get_object_or_404

__all__ = [
    "SocialTargetNestedView",
]


class SocialTargetNestedView(GenericViewSet):

    def get_target_model_class(self):
        raise NotImplementedError

    @property
    def target_id(self):
        return self.kwargs["target_pk"]

    def get_target(self):
        target_model = self.get_target_model_class()
        return get_object_or_404(target_model, id=self.target_id)
