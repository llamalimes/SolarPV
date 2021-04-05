from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products_api', views.ProductAPIView)
router.register('certificates_api', views.CertificateAPIView)
router.register('services_api', views.ServiceAPIView)
router.register('locations_api', views.LocationAPIView)
router.register('clients_api', views.ClientAPIView)
router.register('performancedatas_api', views.PerformanceDataAPIView)
router.register('testsequences_api', views.TestSequenceAPIView)
router.register('teststandards_api', views.TestStandardAPIView)


urlpatterns = [
    path('', views.home_view, name='home'),
    path('portal/', views.portal_view, name='portal'),
    path('', include(router.urls)),

    # Product
    path('product_list/', views.product_list_view, name='list-products'),
    path('add_product/', views.add_product_view, name='add-product'),
    path('product_detail/<product_id>', views.product_detail_view, name='product-detail'),
    path('search_products/', views.search_products_view, name ='search-products'),
    path('product_search_results/', views.product_search_results_view, name ='product-search-results'),
    path('update_product/<product_id>', views.update_product_view, name ='update-product'),
    path('delete_product/<product_id>', views.delete_product_view, name ='delete-product'),

    # Certificate
    path('certificate_list/', views.certificate_list_view, name='list-certificates'),
    path('add_certificate/', views.add_certificate_view, name='add-certificate'),
    path('certificate_detail/<certificate_id>', views.certificate_detail_view, name='certificate-detail'),
    path('search_certificates/', views.search_certificates_view, name ='search-certificates'),
    path('certificate_search_results/', views.certificate_search_results_view, name ='certificate-search-results'),
    path('update_certificate/<certificate_id>', views.update_certificate_view, name ='update-certificate'),
    path('delete_certificate/<certificate_id>', views.delete_certificate_view, name ='delete-certificate'),

    # Service
    path('service_list/', views.service_list_view, name='list-services'),
    path('add_service/', views.add_service_view, name='add-service'),
    path('service_detail/<service_id>', views.service_detail_view, name='service-detail'),
    path('search_services/', views.search_services_view, name ='search-services'),
    path('service_search_results/', views.service_search_results_view, name ='service-search-results'),
    path('update_service/<service_id>', views.update_service_view, name ='update-service'),
    path('delete_service/<service_id>', views.delete_service_view, name ='delete-service'),

    # Location
    path('location_list/', views.location_list_view, name='list-locations'),
    path('add_location/', views.add_location_view, name='add-location'),
    path('location_detail/<location_id>', views.location_detail_view, name='location-detail'),
    path('search_locations/', views.search_locations_view, name ='search-locations'),
    path('location_search_results/', views.location_search_results_view, name ='location-search-results'),
    path('update_location/<location_id>', views.update_location_view, name ='update-location'),
    path('delete_location/<location_id>', views.delete_location_view, name ='delete-location'),

    # Client
    path('client_list/', views.client_list_view, name='list-clients'),
    path('add_client/', views.add_client_view, name='add-client'),
    path('client_detail/<client_id>', views.client_detail_view, name='client-detail'),
    path('search_clients/', views.search_clients_view, name ='search-clients'),
    path('client_search_results/', views.client_search_results_view, name ='client-search-results'),
    path('update_client/<client_id>', views.update_client_view, name ='update-client'),
    path('delete_client/<client_id>', views.delete_client_view, name ='delete-client'),

    # Performance Data
    path('performance_data_list/', views.performance_data_list_view, name='list-performance-datas'),
    path('add_performance_data/', views.add_performance_data_view, name='add-performance-data'),
    path('performance_data_detail/<performance_data_id>', views.performance_data_detail_view, name='performance-data-detail'),
    path('search_performance_datas/', views.search_performance_datas_view, name ='search-performance-datas'),
    path('performance_data_search_results/', views.performance_data_search_results_view, name ='performance-data-search-results'),
    path('update_performance_data/<performance_data_id>', views.update_performance_data_view, name ='update-performance-data'),
    path('delete_performance_data/<performance_data_id>', views.delete_performance_data_view, name ='delete-performance-data'),

    # Test Sequence Data
    path('test_sequence_list/', views.test_sequence_list_view, name='list-test-sequences'),
    path('add_test_sequence/', views.add_test_sequence_view, name='add-test-sequence'),
    path('test_sequence_detail/<test_sequence_id>', views.test_sequence_detail_view, name='test-sequence-detail'),
    path('search_test_sequences/', views.search_test_sequences_view, name ='search-test-sequences'),
    path('test_sequence_search_results/', views.test_sequence_search_results_view, name ='test-sequence-search-results'),
    path('update_test_sequence/<test_sequence_id>', views.update_test_sequence_view, name ='update-test-sequence'),
    path('delete_test_sequence/<test_sequence_id>', views.delete_test_sequence_view, name ='delete-test-sequence'),

    # Test Standard Data
    path('test_standard_list/', views.test_standard_list_view, name='list-test-standards'),
    path('add_test_standard/', views.add_test_standard_view, name='add-test-standard'),
    path('test_standard_detail/<test_standard_id>', views.test_standard_detail_view, name='test-standard-detail'),
    path('search_test_standards/', views.search_test_standards_view, name ='search-test-standards'),
    path('test_standard_search_results/', views.test_standard_search_results_view, name ='test-standard-search-results'),
    path('update_test_standard/<test_standard_id>', views.update_test_standard_view, name ='update-test-standard'),
    path('delete_test_standard/<test_standard_id>', views.delete_test_standard_view, name ='delete-test-standard'),
    

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)