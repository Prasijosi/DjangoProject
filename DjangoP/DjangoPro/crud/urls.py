from django.urls import path
from.views import (classroom_view,add_classroom_view,update_classroom_view,delete_classroom_view,student_view,add_student_view,delete_student_view,update_student_view,
student_profile_view,add_student_profile_view,student_profile_detail_view,student_profile_update_view)


urlpatterns = [
    path("classroom/",classroom_view,name="crud_classroom"),
    path("add-classroom/",add_classroom_view,name="add_classroom"),
    path("update-classroom/<int:id>/",update_classroom_view,name="update_classroom"),
    path("delete-classroom/<int:id>/",delete_classroom_view,name="delete_classroom"),
    path("student/", student_view, name="crud_student"),
    path("add-student/", add_student_view, name="add_student"),
    path("update-student/<int:id>/", update_student_view, name="update_student"),
    path("delete-student/<int:id>/", delete_student_view, name="delete_student"),
    path("student-profile/",student_profile_view,name="student_profile"),
    path("add-student-profile/",add_student_profile_view,name="add_student_profile"),
    path("student-profile-detail/<int:id>/", student_profile_detail_view,name="student_profile_detail"),
    path("student-profile-update/<int:id>/",student_profile_update_view,name="student_profile_update")
]

