from rest_framework.routers import DefaultRouter as DR
from mainapp.views import(
    SchoolView,TeacherView,NewsView,GaleriaView,RewiewView
)

router=DR()
router.register('school', SchoolView, basename='school')
router.register('teacher', TeacherView, basename='teacher')
router.register('galeria', GaleriaView, basename= 'galeria')
router.register('rewiew', RewiewView , basename= 'rewiew')
router.register('news', NewsView, basename= 'news' )

urlpatterns=[]

urlpatterns += router.urls