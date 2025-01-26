from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer

class StudentViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = ['age', 'grade', 'first_name']
    search_fields = ['first_name', 'last_name']

class CourseViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['post'])
    def add_student(self, request, pk=None):
        course = self.get_object()
        student_id = request.data.get('student_id')
        try:
            student = Student.objects.get(id=student_id)
            if student.age < 16:
                return Response({'error': 'Student must be at least 16 years old'}, status=400)
            if course.students.count() >= 30:
                return Response({'error': 'Course student limit exceeded (30)'}, status=400)
            course.students.add(student)
            return Response({'status': 'student added to course'})
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=404)
