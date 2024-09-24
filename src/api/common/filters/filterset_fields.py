__all__ = ["owner_fields", "timestamped_model_fields", "base_model_fields"]

owner_fields = {"owner__id": ["exact"]}

timestamped_model_fields = {
    "created": ["exact", "gt", "lt"],
    "modified": ["exact", "gt", "lt"],
}

base_model_fields = {
    "id": ["exact"],
    **timestamped_model_fields,
}
