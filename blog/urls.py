from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^article/(\d+)/$',"article.views.show_article"),
    url(r'^post_comment/(\d+)/$',"article.views.post_comment"),                   
    url(r'^$',"base_template.views.render_index"),
    url(r'^bootstrap/','templates/bootstrap/'),
    url(r'^article/(\d+)/edit/$',"article.views.edit"),
    url(r'^article/(\d+)/delete/$',"article.views.delete"),
    url(r'^article/(\d+)/edit/save/$',"article.views.save"),
    url(r'^search/$',"base_template.views.search"),
    url(r'^post/$',"article.views.post"),
    url(r'^category/(\d+)$','base_template.views.render_category'),
    url(r'^author/(\w+)$','base_template.views.render_author'),
    url(r'^delete_comment/(\d+)$','article.views.delete_comment'),
    url(r'^feeds/$','base_template.views.render_feeds'),
    
    
)
urlpatterns += patterns('',
    url(r'^resources2/(?P<path>.*)$','django.views.static.serve',{'document_root':'resources2'}),
    url(r'^html/(?P<path>.*)$','django.views.static.serve',{'document_root':'html'}),
    url(r'^upload/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.UPLOAD_PATH}),                     
)
