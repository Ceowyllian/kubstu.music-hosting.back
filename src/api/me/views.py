from api.common import SCHEMA_TAG_ME, APIView, IsAuthenticated, Response, extend_schema
from api.me.serializers import MeSerializer
from db.person.models import Person

__all__ = [
    "MeView",
]


@extend_schema(tags=[SCHEMA_TAG_ME])
class MeView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(responses={200: MeSerializer(many=False)})
    def get(self, request, *args, **kwargs):
        person = Person.objects.get(user=request.user)
        output = MeSerializer(person)
        return Response(output.data)
