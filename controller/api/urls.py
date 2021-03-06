from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url

from api import routers
from api import views


router = routers.ApiRouter()

# Add the generated REST URLs and login/logout endpoint
urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
    # application release components
    url(r'^apps/(?P<id>{})/config/?'.format(settings.APP_URL_REGEX),
        views.AppConfigViewSet.as_view({'get': 'retrieve', 'post': 'create'})),
    url(r'^apps/(?P<id>{})/builds/(?P<uuid>[-_\w]+)/?'.format(settings.APP_URL_REGEX),
        views.AppBuildViewSet.as_view({'get': 'retrieve'})),
    url(r'^apps/(?P<id>{})/builds/?'.format(settings.APP_URL_REGEX),
        views.AppBuildViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(r'^apps/(?P<id>{})/releases/v(?P<version>[0-9]+)/?'.format(settings.APP_URL_REGEX),
        views.AppReleaseViewSet.as_view({'get': 'retrieve'})),
    url(r'^apps/(?P<id>{})/releases/rollback/?'.format(settings.APP_URL_REGEX),
        views.AppReleaseViewSet.as_view({'post': 'rollback'})),
    url(r'^apps/(?P<id>{})/releases/?'.format(settings.APP_URL_REGEX),
        views.AppReleaseViewSet.as_view({'get': 'list'})),
    # application infrastructure
    url(r'^apps/(?P<id>{})/containers/(?P<type>[-_\w]+)/(?P<num>[-_\w]+)/?'.format(
        settings.APP_URL_REGEX),
        views.AppContainerViewSet.as_view({'get': 'retrieve'})),
    url(r'^apps/(?P<id>{})/containers/(?P<type>[-_\w.]+)/?'.format(settings.APP_URL_REGEX),
        views.AppContainerViewSet.as_view({'get': 'list'})),
    url(r'^apps/(?P<id>{})/containers/?'.format(settings.APP_URL_REGEX),
        views.AppContainerViewSet.as_view({'get': 'list'})),
    # application domains
    url(r'^apps/(?P<id>{})/domains/(?P<domain>[-\._\w]+)/?'.format(settings.APP_URL_REGEX),
        views.DomainViewSet.as_view({'delete': 'destroy'})),
    url(r'^apps/(?P<id>{})/domains/?'.format(settings.APP_URL_REGEX),
        views.DomainViewSet.as_view({'post': 'create', 'get': 'list'})),
    # application actions
    url(r'^apps/(?P<id>{})/scale/?'.format(settings.APP_URL_REGEX),
        views.AppViewSet.as_view({'post': 'scale'})),
    url(r'^apps/(?P<id>{})/logs/?'.format(settings.APP_URL_REGEX),
        views.AppViewSet.as_view({'get': 'logs'})),
    url(r'^apps/(?P<id>{})/run/?'.format(settings.APP_URL_REGEX),
        views.AppViewSet.as_view({'post': 'run'})),
    # apps sharing
    url(r'^apps/(?P<id>{})/perms/(?P<username>[-_\w]+)/?'.format(settings.APP_URL_REGEX),
        views.AppPermsViewSet.as_view({'delete': 'destroy'})),
    url(r'^apps/(?P<id>{})/perms/?'.format(settings.APP_URL_REGEX),
        views.AppPermsViewSet.as_view({'get': 'list', 'post': 'create'})),
    # apps base endpoint
    url(r'^apps/(?P<id>{})/?'.format(settings.APP_URL_REGEX),
        views.AppViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    url(r'^apps/?',
        views.AppViewSet.as_view({'get': 'list', 'post': 'create'})),
    # key
    url(r'^keys/(?P<id>.+)/?',
        views.KeyViewSet.as_view({
            'get': 'retrieve', 'delete': 'destroy'})),
    url(r'^keys/?',
        views.KeyViewSet.as_view({'get': 'list', 'post': 'create'})),
    # hooks
    url(r'^hooks/push/?',
        views.PushHookViewSet.as_view({'post': 'create'})),
    url(r'^hooks/build/?',
        views.BuildHookViewSet.as_view({'post': 'create'})),
    url(r'^hooks/config/?',
        views.ConfigHookViewSet.as_view({'post': 'create'})),
    # authn / authz
    url(r'^auth/register/?',
        views.UserRegistrationView.as_view({'post': 'create'})),
    url(r'^auth/cancel/?',
        views.UserManagementView.as_view({'delete': 'destroy'})),
    url(r'^auth/passwd/?',
        views.UserManagementView.as_view({'post': 'passwd'})),
    url(r'^auth/login/',
        'rest_framework.authtoken.views.obtain_auth_token'),
    # admin sharing
    url(r'^admin/perms/(?P<username>[-_\w]+)/?',
        views.AdminPermsViewSet.as_view({'delete': 'destroy'})),
    url(r'^admin/perms/?',
        views.AdminPermsViewSet.as_view({'get': 'list', 'post': 'create'})),
)
