
from . import views
from django.conf.urls import url, include
from .autocomplete import *

urlpatterns = [
    url(r'^register_question', views.register_question, name='register_question'),
    url(r'^list_questions', views.list_questions, name = 'list_questions'),
    url(r'^detail_question/(?P<question_id>[0-9]+)', views.detail, name='detail_question'),
    url(r'^edit_question/(?P<question_id>[0-9]+)',views.edit_question, name = 'edit_question'),
    url(r'^distribute_question/(?P<question_id>[0-9]+)',views.distribute_question, name = 'distribute_question'),
    url(r'^open_question/(?P<question_id>[0-9]+)',views.open_question, name = 'open_question'),
    url(r'^reserve_question/(?P<question_id>[0-9]+)',views.reserve_question, name = 'reserve_question'),
    url(r'^assign_question/(?P<question_id>[0-9]+)',views.assign_question, name = 'assign_question'),
    url(r'round_up_question/(?P<question_id>[0-9]+)',views.round_up_question, name = 'round_up_question'),
    url(r'deny_question/(?P<question_id>[0-9]+)',views.deny_question, name = 'deny_question'),
    url(r'revoke_question/(?P<question_id>[0-9]+)',views.revoke_question, name = 'revoke_question'),
    url(r'distribute_intake/(?P<question_id>[0-9]+)',views.distribute_intake, name = 'distribute_intake'),
    url(r'internal_remark/(?P<question_id>[0-9]+)', views.internal_remark, name = 'internal_remark'),
    url(r'edit_meta_info/(?P<question_id>[0-9]+)', views.edit_meta_info, name ='edit_meta_info'),
    url(r'register_institution/(?P<question_id>[0-9]+)', views.register_institution, name ='register_institution'),
    url(r'^search/', include('haystack.urls')),

    url(r'^institution-autocomplete/$',
        InstitutionAutocomplete.as_view(),
        name = 'institution-autocomplete'),


    url(r'^study_field-autocomplete/$',
        StudyFieldAutocomplete.as_view(create_field = 'study_field'),
        name='study_field-autocomplete'),


    url(r'^subject-autocomplete/$',
    SubjectAutocomplete.as_view(create_field='subject'),
    name='subject-autocomplete'),
    ]

