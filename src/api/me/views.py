from api.common import SCHEMA_TAG_ME, APIView, IsAuthenticated, Response, extend_schema
from api.me.serializers import MeSerializer, PersonUpdateSerializer
from db.person.models import Person
from services.person import update_person

__all__ = [
    "MeView",
]


@extend_schema(tags=[SCHEMA_TAG_ME])
class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Person.objects.get(user=self.request.user)

    @extend_schema(
        responses={200: MeSerializer(many=False)},
    )
    def get(self, request, *args, **kwargs):
        person = self.get_object()
        output = MeSerializer(person)
        return Response(output.data)

    @extend_schema(
        request=PersonUpdateSerializer(partial=True),
        responses={200: MeSerializer},
    )
    def patch(self, request, *args, **kwargs):
        person = self.get_object()
        input_ = PersonUpdateSerializer(data=request.data, partial=True)
        input_.is_valid(raise_exception=True)
        person = update_person(instance=person, **input_.validated_data)
        output = MeSerializer(person)
        return Response(output.data)
