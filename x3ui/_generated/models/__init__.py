"""Contains all the data models used in inputs/outputs"""

from .all_setting import AllSetting
from .all_setting_view import AllSettingView
from .amnezia_wg_logs import AmneziaWGLogs
from .api_token import ApiToken
from .api_token_view import ApiTokenView
from .client import Client
from .client_allowed_i_ps_by_inbound import ClientAllowedIPsByInbound
from .client_inbound import ClientInbound
from .client_record import ClientRecord
from .client_reverse import ClientReverse
from .client_traffic import ClientTraffic
from .client_traffic_reset import ClientTrafficReset
from .clients_active_inbounds import ClientsActiveInbounds
from .clients_add_request import ClientsAddRequest
from .clients_add_request_client import ClientsAddRequestClient
from .clients_attach_request import ClientsAttachRequest
from .clients_bulk_adjust import ClientsBulkAdjust
from .clients_bulk_adjust_request import ClientsBulkAdjustRequest
from .clients_bulk_adjust_skipped_item import ClientsBulkAdjustSkippedItem
from .clients_bulk_attach import ClientsBulkAttach
from .clients_bulk_attach_request import ClientsBulkAttachRequest
from .clients_bulk_create import ClientsBulkCreate
from .clients_bulk_create_skipped_item import ClientsBulkCreateSkippedItem
from .clients_bulk_del import ClientsBulkDel
from .clients_bulk_del_request import ClientsBulkDelRequest
from .clients_bulk_del_skipped_item import ClientsBulkDelSkippedItem
from .clients_bulk_detach import ClientsBulkDetach
from .clients_bulk_detach_request import ClientsBulkDetachRequest
from .clients_bulk_disable import ClientsBulkDisable
from .clients_bulk_disable_request import ClientsBulkDisableRequest
from .clients_bulk_disable_skipped_item import ClientsBulkDisableSkippedItem
from .clients_bulk_enable import ClientsBulkEnable
from .clients_bulk_enable_request import ClientsBulkEnableRequest
from .clients_bulk_enable_skipped_item import ClientsBulkEnableSkippedItem
from .clients_bulk_reset_traffic import ClientsBulkResetTraffic
from .clients_bulk_reset_traffic_request import ClientsBulkResetTrafficRequest
from .clients_client_ips_by_guid import ClientsClientIpsByGuid
from .clients_client_ips_by_guid_a1b2 import ClientsClientIpsByGuidA1B2
from .clients_client_ips_by_guid_a1b2_user_1_item import (
    ClientsClientIpsByGuidA1B2User1Item,
)
from .clients_del_depleted import ClientsDelDepleted
from .clients_del_orphans import ClientsDelOrphans
from .clients_detach_request import ClientsDetachRequest
from .clients_export_item import ClientsExportItem
from .clients_export_item_client import ClientsExportItemClient
from .clients_groups_bulk_add import ClientsGroupsBulkAdd
from .clients_groups_bulk_add_request import ClientsGroupsBulkAddRequest
from .clients_groups_bulk_remove import ClientsGroupsBulkRemove
from .clients_groups_bulk_remove_request import ClientsGroupsBulkRemoveRequest
from .clients_groups_create import ClientsGroupsCreate
from .clients_groups_create_request import ClientsGroupsCreateRequest
from .clients_groups_delete import ClientsGroupsDelete
from .clients_groups_delete_request import ClientsGroupsDeleteRequest
from .clients_groups_item import ClientsGroupsItem
from .clients_groups_rename import ClientsGroupsRename
from .clients_groups_rename_request import ClientsGroupsRenameRequest
from .clients_groups_reset_traffic import ClientsGroupsResetTraffic
from .clients_groups_reset_traffic_request import ClientsGroupsResetTrafficRequest
from .clients_hwids_item import ClientsHwidsItem
from .clients_import import ClientsImport
from .clients_import_request import ClientsImportRequest
from .clients_import_skipped_item import ClientsImportSkippedItem
from .clients_last_online import ClientsLastOnline
from .clients_list_item import ClientsListItem
from .clients_list_item_traffic import ClientsListItemTraffic
from .clients_list_paged import ClientsListPaged
from .clients_list_paged_items_item import ClientsListPagedItemsItem
from .clients_list_paged_items_item_traffic import ClientsListPagedItemsItemTraffic
from .clients_list_paged_summary import ClientsListPagedSummary
from .clients_onlines_by_guid import ClientsOnlinesByGuid
from .clients_update_request import ClientsUpdateRequest
from .clients_update_traffic_request import ClientsUpdateTrafficRequest
from .delete_panel_api_clients_hwids_email_id_response_200 import (
    DeletePanelApiClientsHwidsEmailIdResponse200,
)
from .delete_panel_api_clients_hwids_email_response_200 import (
    DeletePanelApiClientsHwidsEmailResponse200,
)
from .delete_panel_api_sub_balancers_id_response_200 import (
    DeletePanelApiSubBalancersIdResponse200,
)
from .delete_panel_api_xray_outbound_subs_id_response_200 import (
    DeletePanelApiXrayOutboundSubsIdResponse200,
)
from .fallback_parent_info import FallbackParentInfo
from .geo_category import GeoCategory
from .geo_category_page import GeoCategoryPage
from .geo_entry import GeoEntry
from .geo_entry_page import GeoEntryPage
from .geo_file import GeoFile
from .geodata_token_issue import GeodataTokenIssue
from .get_clash_path_subid_response_200 import GetClashPathSubidResponse200
from .get_csrf_token_response_200 import GetCsrfTokenResponse200
from .get_json_path_subid_response_200 import GetJsonPathSubidResponse200
from .get_panel_api_clients_export_response_200 import (
    GetPanelApiClientsExportResponse200,
)
from .get_panel_api_clients_get_email_response_200 import (
    GetPanelApiClientsGetEmailResponse200,
)
from .get_panel_api_clients_get_tg_id_tg_id_response_200 import (
    GetPanelApiClientsGetTgIdTgIdResponse200,
)
from .get_panel_api_clients_groups_name_emails_response_200 import (
    GetPanelApiClientsGroupsNameEmailsResponse200,
)
from .get_panel_api_clients_groups_response_200 import (
    GetPanelApiClientsGroupsResponse200,
)
from .get_panel_api_clients_links_email_response_200 import (
    GetPanelApiClientsLinksEmailResponse200,
)
from .get_panel_api_clients_list_paged_response_200 import (
    GetPanelApiClientsListPagedResponse200,
)
from .get_panel_api_clients_list_response_200 import GetPanelApiClientsListResponse200
from .get_panel_api_clients_sub_links_sub_id_response_200 import (
    GetPanelApiClientsSubLinksSubIdResponse200,
)
from .get_panel_api_clients_traffic_email_response_200 import (
    GetPanelApiClientsTrafficEmailResponse200,
)
from .get_panel_api_hosts_by_inbound_inbound_id_response_200 import (
    GetPanelApiHostsByInboundInboundIdResponse200,
)
from .get_panel_api_hosts_get_group_id_response_200 import (
    GetPanelApiHostsGetGroupIdResponse200,
)
from .get_panel_api_hosts_list_response_200 import GetPanelApiHostsListResponse200
from .get_panel_api_hosts_tags_response_200 import GetPanelApiHostsTagsResponse200
from .get_panel_api_inbounds_all_links_response_200 import (
    GetPanelApiInboundsAllLinksResponse200,
)
from .get_panel_api_inbounds_get_id_response_200 import (
    GetPanelApiInboundsGetIdResponse200,
)
from .get_panel_api_inbounds_id_fallbacks_response_200 import (
    GetPanelApiInboundsIdFallbacksResponse200,
)
from .get_panel_api_inbounds_list_response_200 import GetPanelApiInboundsListResponse200
from .get_panel_api_inbounds_list_slim_response_200 import (
    GetPanelApiInboundsListSlimResponse200,
)
from .get_panel_api_inbounds_options_response_200 import (
    GetPanelApiInboundsOptionsResponse200,
)
from .get_panel_api_nodes_get_id_response_200 import GetPanelApiNodesGetIdResponse200
from .get_panel_api_nodes_history_id_metric_bucket_response_200 import (
    GetPanelApiNodesHistoryIdMetricBucketResponse200,
)
from .get_panel_api_nodes_list_response_200 import GetPanelApiNodesListResponse200
from .get_panel_api_nodes_web_cert_id_response_200 import (
    GetPanelApiNodesWebCertIdResponse200,
)
from .get_panel_api_openapi_json_response_200 import GetPanelApiOpenapiJsonResponse200
from .get_panel_api_server_client_ips_response_200 import (
    GetPanelApiServerClientIpsResponse200,
)
from .get_panel_api_server_cpu_history_bucket_response_200 import (
    GetPanelApiServerCpuHistoryBucketResponse200,
)
from .get_panel_api_server_descendants_response_200 import (
    GetPanelApiServerDescendantsResponse200,
)
from .get_panel_api_server_fail_2_ban_status_response_200 import (
    GetPanelApiServerFail2BanStatusResponse200,
)
from .get_panel_api_server_get_config_json_response_200 import (
    GetPanelApiServerGetConfigJsonResponse200,
)
from .get_panel_api_server_get_db_response_200 import GetPanelApiServerGetDbResponse200
from .get_panel_api_server_get_migration_response_200 import (
    GetPanelApiServerGetMigrationResponse200,
)
from .get_panel_api_server_get_new_uuid_response_200 import (
    GetPanelApiServerGetNewUUIDResponse200,
)
from .get_panel_api_server_get_new_vless_enc_response_200 import (
    GetPanelApiServerGetNewVlessEncResponse200,
)
from .get_panel_api_server_get_new_x25519_cert_response_200 import (
    GetPanelApiServerGetNewX25519CertResponse200,
)
from .get_panel_api_server_get_newmldsa_65_response_200 import (
    GetPanelApiServerGetNewmldsa65Response200,
)
from .get_panel_api_server_get_newmlkem_768_response_200 import (
    GetPanelApiServerGetNewmlkem768Response200,
)
from .get_panel_api_server_get_panel_update_info_response_200 import (
    GetPanelApiServerGetPanelUpdateInfoResponse200,
)
from .get_panel_api_server_get_update_status_response_200 import (
    GetPanelApiServerGetUpdateStatusResponse200,
)
from .get_panel_api_server_get_web_cert_files_response_200 import (
    GetPanelApiServerGetWebCertFilesResponse200,
)
from .get_panel_api_server_get_xray_version_response_200 import (
    GetPanelApiServerGetXrayVersionResponse200,
)
from .get_panel_api_server_history_metric_bucket_response_200 import (
    GetPanelApiServerHistoryMetricBucketResponse200,
)
from .get_panel_api_server_status_response_200 import GetPanelApiServerStatusResponse200
from .get_panel_api_server_xray_metrics_history_metric_bucket_response_200 import (
    GetPanelApiServerXrayMetricsHistoryMetricBucketResponse200,
)
from .get_panel_api_server_xray_metrics_state_response_200 import (
    GetPanelApiServerXrayMetricsStateResponse200,
)
from .get_panel_api_server_xray_observatory_history_tag_bucket_response_200 import (
    GetPanelApiServerXrayObservatoryHistoryTagBucketResponse200,
)
from .get_panel_api_server_xray_observatory_response_200 import (
    GetPanelApiServerXrayObservatoryResponse200,
)
from .get_panel_api_setting_api_tokens_response_200 import (
    GetPanelApiSettingApiTokensResponse200,
)
from .get_panel_api_setting_get_default_json_config_response_200 import (
    GetPanelApiSettingGetDefaultJsonConfigResponse200,
)
from .get_panel_api_sub_balancers_response_200 import GetPanelApiSubBalancersResponse200
from .get_panel_api_xray_geodata_categories_response_200 import (
    GetPanelApiXrayGeodataCategoriesResponse200,
)
from .get_panel_api_xray_geodata_entries_response_200 import (
    GetPanelApiXrayGeodataEntriesResponse200,
)
from .get_panel_api_xray_geodata_files_response_200 import (
    GetPanelApiXrayGeodataFilesResponse200,
)
from .get_panel_api_xray_get_default_json_config_response_200 import (
    GetPanelApiXrayGetDefaultJsonConfigResponse200,
)
from .get_panel_api_xray_get_outbounds_traffic_response_200 import (
    GetPanelApiXrayGetOutboundsTrafficResponse200,
)
from .get_panel_api_xray_get_xray_result_response_200 import (
    GetPanelApiXrayGetXrayResultResponse200,
)
from .get_panel_api_xray_outbound_subs_response_200 import (
    GetPanelApiXrayOutboundSubsResponse200,
)
from .get_sub_path_subid_response_200 import GetSubPathSubidResponse200
from .get_ws_response_200 import GetWsResponse200
from .history_of_seeders import HistoryOfSeeders
from .host import Host
from .host_group import HostGroup
from .host_group_mihomo_ip_version import HostGroupMihomoIpVersion
from .host_group_security import HostGroupSecurity
from .host_mihomo_ip_version import HostMihomoIpVersion
from .host_security import HostSecurity
from .hosts_add_request import HostsAddRequest
from .hosts_bulk_add_request import HostsBulkAddRequest
from .hosts_bulk_del_request import HostsBulkDelRequest
from .hosts_bulk_set_enable_request import HostsBulkSetEnableRequest
from .hosts_reorder_request import HostsReorderRequest
from .hosts_set_enable_request import HostsSetEnableRequest
from .hosts_update_request import HostsUpdateRequest
from .inbound import Inbound
from .inbound_client_ips import InboundClientIps
from .inbound_fallback import InboundFallback
from .inbound_option import InboundOption
from .inbound_protocol import InboundProtocol
from .inbound_share_addr_strategy import InboundShareAddrStrategy
from .inbound_traffic_reset import InboundTrafficReset
from .inbounds_add_request import InboundsAddRequest
from .inbounds_add_request_settings import InboundsAddRequestSettings
from .inbounds_add_request_settings_clients_item import (
    InboundsAddRequestSettingsClientsItem,
)
from .inbounds_add_request_sniffing import InboundsAddRequestSniffing
from .inbounds_add_request_stream_settings import InboundsAddRequestStreamSettings
from .inbounds_add_request_stream_settings_reality_settings import (
    InboundsAddRequestStreamSettingsRealitySettings,
)
from .inbounds_bulk_del import InboundsBulkDel
from .inbounds_bulk_del_request import InboundsBulkDelRequest
from .inbounds_bulk_del_skipped_item import InboundsBulkDelSkippedItem
from .inbounds_del_all_clients import InboundsDelAllClients
from .inbounds_fallbacks_item import InboundsFallbacksItem
from .inbounds_fallbacks_request import InboundsFallbacksRequest
from .inbounds_fallbacks_request_fallbacks_item import (
    InboundsFallbacksRequestFallbacksItem,
)
from .inbounds_list_slim_item import InboundsListSlimItem
from .inbounds_list_slim_item_settings import InboundsListSlimItemSettings
from .inbounds_list_slim_item_settings_clients_item import (
    InboundsListSlimItemSettingsClientsItem,
)
from .inbounds_push_client_traffics_request import InboundsPushClientTrafficsRequest
from .inbounds_push_client_traffics_request_traffics_item import (
    InboundsPushClientTrafficsRequestTrafficsItem,
)
from .inbounds_set_enable_request import InboundsSetEnableRequest
from .inbounds_sub_sort_index_request import InboundsSubSortIndexRequest
from .msg import Msg
from .node import Node
from .node_inbound_sync_mode import NodeInboundSyncMode
from .node_mutation_request import NodeMutationRequest
from .node_mutation_request_inbound_sync_mode import NodeMutationRequestInboundSyncMode
from .node_mutation_request_scheme import NodeMutationRequestScheme
from .node_mutation_request_tls_verify_mode import NodeMutationRequestTlsVerifyMode
from .node_scheme import NodeScheme
from .node_tls_verify_mode import NodeTlsVerifyMode
from .node_view import NodeView
from .nodes_add_request import NodesAddRequest
from .nodes_cert_fingerprint_request import NodesCertFingerprintRequest
from .nodes_inbounds_item import NodesInboundsItem
from .nodes_inbounds_request import NodesInboundsRequest
from .nodes_mtls_ca import NodesMtlsCa
from .nodes_mtls_trust_ca_request import NodesMtlsTrustCARequest
from .nodes_set_enable_request import NodesSetEnableRequest
from .nodes_test_request import NodesTestRequest
from .nodes_update_panel_item import NodesUpdatePanelItem
from .nodes_update_panel_request import NodesUpdatePanelRequest
from .nodes_update_request import NodesUpdateRequest
from .nodes_web_cert import NodesWebCert
from .outbound_traffics import OutboundTraffics
from .panel_update_status import PanelUpdateStatus
from .peer_activity import PeerActivity
from .post_get_two_factor_enable_response_200 import PostGetTwoFactorEnableResponse200
from .post_login_body import PostLoginBody
from .post_login_response_200 import PostLoginResponse200
from .post_login_response_400 import PostLoginResponse400
from .post_logout_response_200 import PostLogoutResponse200
from .post_panel_api_backuptotgbot_response_200 import (
    PostPanelApiBackuptotgbotResponse200,
)
from .post_panel_api_clients_active_inbounds_response_200 import (
    PostPanelApiClientsActiveInboundsResponse200,
)
from .post_panel_api_clients_add_response_200 import PostPanelApiClientsAddResponse200
from .post_panel_api_clients_bulk_adjust_response_200 import (
    PostPanelApiClientsBulkAdjustResponse200,
)
from .post_panel_api_clients_bulk_attach_response_200 import (
    PostPanelApiClientsBulkAttachResponse200,
)
from .post_panel_api_clients_bulk_create_body_item import (
    PostPanelApiClientsBulkCreateBodyItem,
)
from .post_panel_api_clients_bulk_create_body_item_client import (
    PostPanelApiClientsBulkCreateBodyItemClient,
)
from .post_panel_api_clients_bulk_create_response_200 import (
    PostPanelApiClientsBulkCreateResponse200,
)
from .post_panel_api_clients_bulk_del_response_200 import (
    PostPanelApiClientsBulkDelResponse200,
)
from .post_panel_api_clients_bulk_detach_response_200 import (
    PostPanelApiClientsBulkDetachResponse200,
)
from .post_panel_api_clients_bulk_disable_response_200 import (
    PostPanelApiClientsBulkDisableResponse200,
)
from .post_panel_api_clients_bulk_enable_response_200 import (
    PostPanelApiClientsBulkEnableResponse200,
)
from .post_panel_api_clients_bulk_reset_traffic_response_200 import (
    PostPanelApiClientsBulkResetTrafficResponse200,
)
from .post_panel_api_clients_clear_ips_email_response_200 import (
    PostPanelApiClientsClearIpsEmailResponse200,
)
from .post_panel_api_clients_client_ips_by_guid_response_200 import (
    PostPanelApiClientsClientIpsByGuidResponse200,
)
from .post_panel_api_clients_del_depleted_response_200 import (
    PostPanelApiClientsDelDepletedResponse200,
)
from .post_panel_api_clients_del_email_response_200 import (
    PostPanelApiClientsDelEmailResponse200,
)
from .post_panel_api_clients_del_orphans_response_200 import (
    PostPanelApiClientsDelOrphansResponse200,
)
from .post_panel_api_clients_email_attach_response_200 import (
    PostPanelApiClientsEmailAttachResponse200,
)
from .post_panel_api_clients_email_detach_response_200 import (
    PostPanelApiClientsEmailDetachResponse200,
)
from .post_panel_api_clients_email_external_links_body import (
    PostPanelApiClientsEmailExternalLinksBody,
)
from .post_panel_api_clients_email_external_links_body_external_links_item import (
    PostPanelApiClientsEmailExternalLinksBodyExternalLinksItem,
)
from .post_panel_api_clients_email_external_links_response_200 import (
    PostPanelApiClientsEmailExternalLinksResponse200,
)
from .post_panel_api_clients_groups_bulk_add_response_200 import (
    PostPanelApiClientsGroupsBulkAddResponse200,
)
from .post_panel_api_clients_groups_bulk_remove_response_200 import (
    PostPanelApiClientsGroupsBulkRemoveResponse200,
)
from .post_panel_api_clients_groups_create_response_200 import (
    PostPanelApiClientsGroupsCreateResponse200,
)
from .post_panel_api_clients_groups_delete_response_200 import (
    PostPanelApiClientsGroupsDeleteResponse200,
)
from .post_panel_api_clients_groups_rename_response_200 import (
    PostPanelApiClientsGroupsRenameResponse200,
)
from .post_panel_api_clients_groups_reset_traffic_response_200 import (
    PostPanelApiClientsGroupsResetTrafficResponse200,
)
from .post_panel_api_clients_hwids_email_response_200 import (
    PostPanelApiClientsHwidsEmailResponse200,
)
from .post_panel_api_clients_import_response_200 import (
    PostPanelApiClientsImportResponse200,
)
from .post_panel_api_clients_ips_email_response_200 import (
    PostPanelApiClientsIpsEmailResponse200,
)
from .post_panel_api_clients_last_online_response_200 import (
    PostPanelApiClientsLastOnlineResponse200,
)
from .post_panel_api_clients_onlines_by_guid_response_200 import (
    PostPanelApiClientsOnlinesByGuidResponse200,
)
from .post_panel_api_clients_onlines_response_200 import (
    PostPanelApiClientsOnlinesResponse200,
)
from .post_panel_api_clients_reset_all_traffics_response_200 import (
    PostPanelApiClientsResetAllTrafficsResponse200,
)
from .post_panel_api_clients_reset_traffic_email_response_200 import (
    PostPanelApiClientsResetTrafficEmailResponse200,
)
from .post_panel_api_clients_update_email_response_200 import (
    PostPanelApiClientsUpdateEmailResponse200,
)
from .post_panel_api_clients_update_traffic_email_response_200 import (
    PostPanelApiClientsUpdateTrafficEmailResponse200,
)
from .post_panel_api_hosts_add_response_200 import PostPanelApiHostsAddResponse200
from .post_panel_api_hosts_bulk_add_response_200 import (
    PostPanelApiHostsBulkAddResponse200,
)
from .post_panel_api_hosts_bulk_del_response_200 import (
    PostPanelApiHostsBulkDelResponse200,
)
from .post_panel_api_hosts_bulk_set_enable_response_200 import (
    PostPanelApiHostsBulkSetEnableResponse200,
)
from .post_panel_api_hosts_del_group_id_response_200 import (
    PostPanelApiHostsDelGroupIdResponse200,
)
from .post_panel_api_hosts_reorder_response_200 import (
    PostPanelApiHostsReorderResponse200,
)
from .post_panel_api_hosts_set_enable_group_id_response_200 import (
    PostPanelApiHostsSetEnableGroupIdResponse200,
)
from .post_panel_api_hosts_update_group_id_response_200 import (
    PostPanelApiHostsUpdateGroupIdResponse200,
)
from .post_panel_api_inbounds_add_response_200 import PostPanelApiInboundsAddResponse200
from .post_panel_api_inbounds_add_response_400 import PostPanelApiInboundsAddResponse400
from .post_panel_api_inbounds_bulk_del_response_200 import (
    PostPanelApiInboundsBulkDelResponse200,
)
from .post_panel_api_inbounds_del_id_response_200 import (
    PostPanelApiInboundsDelIdResponse200,
)
from .post_panel_api_inbounds_id_del_all_clients_response_200 import (
    PostPanelApiInboundsIdDelAllClientsResponse200,
)
from .post_panel_api_inbounds_id_fallbacks_response_200 import (
    PostPanelApiInboundsIdFallbacksResponse200,
)
from .post_panel_api_inbounds_id_reset_traffic_response_200 import (
    PostPanelApiInboundsIdResetTrafficResponse200,
)
from .post_panel_api_inbounds_id_sub_sort_index_response_200 import (
    PostPanelApiInboundsIdSubSortIndexResponse200,
)
from .post_panel_api_inbounds_import_response_200 import (
    PostPanelApiInboundsImportResponse200,
)
from .post_panel_api_inbounds_push_client_traffics_response_200 import (
    PostPanelApiInboundsPushClientTrafficsResponse200,
)
from .post_panel_api_inbounds_reset_all_traffics_response_200 import (
    PostPanelApiInboundsResetAllTrafficsResponse200,
)
from .post_panel_api_inbounds_set_enable_id_response_200 import (
    PostPanelApiInboundsSetEnableIdResponse200,
)
from .post_panel_api_inbounds_update_id_response_200 import (
    PostPanelApiInboundsUpdateIdResponse200,
)
from .post_panel_api_nodes_add_response_200 import PostPanelApiNodesAddResponse200
from .post_panel_api_nodes_cert_fingerprint_response_200 import (
    PostPanelApiNodesCertFingerprintResponse200,
)
from .post_panel_api_nodes_del_id_response_200 import PostPanelApiNodesDelIdResponse200
from .post_panel_api_nodes_inbounds_response_200 import (
    PostPanelApiNodesInboundsResponse200,
)
from .post_panel_api_nodes_mtls_ca_response_200 import (
    PostPanelApiNodesMtlsCaResponse200,
)
from .post_panel_api_nodes_mtls_reload_client_response_200 import (
    PostPanelApiNodesMtlsReloadClientResponse200,
)
from .post_panel_api_nodes_mtls_trust_ca_response_200 import (
    PostPanelApiNodesMtlsTrustCAResponse200,
)
from .post_panel_api_nodes_probe_id_response_200 import (
    PostPanelApiNodesProbeIdResponse200,
)
from .post_panel_api_nodes_set_enable_id_response_200 import (
    PostPanelApiNodesSetEnableIdResponse200,
)
from .post_panel_api_nodes_test_response_200 import PostPanelApiNodesTestResponse200
from .post_panel_api_nodes_update_id_response_200 import (
    PostPanelApiNodesUpdateIdResponse200,
)
from .post_panel_api_nodes_update_panel_response_200 import (
    PostPanelApiNodesUpdatePanelResponse200,
)
from .post_panel_api_server_amneziawglogs_count_body import (
    PostPanelApiServerAmneziawglogsCountBody,
)
from .post_panel_api_server_amneziawglogs_count_response_200 import (
    PostPanelApiServerAmneziawglogsCountResponse200,
)
from .post_panel_api_server_client_ips_response_200 import (
    PostPanelApiServerClientIpsResponse200,
)
from .post_panel_api_server_get_cert_hash_body import PostPanelApiServerGetCertHashBody
from .post_panel_api_server_get_cert_hash_response_200 import (
    PostPanelApiServerGetCertHashResponse200,
)
from .post_panel_api_server_get_new_ech_cert_body import (
    PostPanelApiServerGetNewEchCertBody,
)
from .post_panel_api_server_get_new_ech_cert_response_200 import (
    PostPanelApiServerGetNewEchCertResponse200,
)
from .post_panel_api_server_get_remote_cert_hash_body import (
    PostPanelApiServerGetRemoteCertHashBody,
)
from .post_panel_api_server_get_remote_cert_hash_response_200 import (
    PostPanelApiServerGetRemoteCertHashResponse200,
)
from .post_panel_api_server_import_db_response_200 import (
    PostPanelApiServerImportDBResponse200,
)
from .post_panel_api_server_install_xray_version_response_200 import (
    PostPanelApiServerInstallXrayVersionResponse200,
)
from .post_panel_api_server_logs_count_response_200 import (
    PostPanelApiServerLogsCountResponse200,
)
from .post_panel_api_server_restart_xray_service_response_200 import (
    PostPanelApiServerRestartXrayServiceResponse200,
)
from .post_panel_api_server_restart_xray_service_response_400 import (
    PostPanelApiServerRestartXrayServiceResponse400,
)
from .post_panel_api_server_scan_reality_target_body import (
    PostPanelApiServerScanRealityTargetBody,
)
from .post_panel_api_server_scan_reality_target_response_200 import (
    PostPanelApiServerScanRealityTargetResponse200,
)
from .post_panel_api_server_scan_reality_targets_body import (
    PostPanelApiServerScanRealityTargetsBody,
)
from .post_panel_api_server_scan_reality_targets_response_200 import (
    PostPanelApiServerScanRealityTargetsResponse200,
)
from .post_panel_api_server_set_update_channel_body import (
    PostPanelApiServerSetUpdateChannelBody,
)
from .post_panel_api_server_set_update_channel_response_200 import (
    PostPanelApiServerSetUpdateChannelResponse200,
)
from .post_panel_api_server_stop_xray_service_response_200 import (
    PostPanelApiServerStopXrayServiceResponse200,
)
from .post_panel_api_server_stop_xray_service_response_400 import (
    PostPanelApiServerStopXrayServiceResponse400,
)
from .post_panel_api_server_update_geofile_body import (
    PostPanelApiServerUpdateGeofileBody,
)
from .post_panel_api_server_update_geofile_file_name_response_200 import (
    PostPanelApiServerUpdateGeofileFileNameResponse200,
)
from .post_panel_api_server_update_geofile_response_200 import (
    PostPanelApiServerUpdateGeofileResponse200,
)
from .post_panel_api_server_update_panel_response_200 import (
    PostPanelApiServerUpdatePanelResponse200,
)
from .post_panel_api_server_xraylogs_count_body import (
    PostPanelApiServerXraylogsCountBody,
)
from .post_panel_api_server_xraylogs_count_response_200 import (
    PostPanelApiServerXraylogsCountResponse200,
)
from .post_panel_api_setting_all_response_200 import PostPanelApiSettingAllResponse200
from .post_panel_api_setting_api_tokens_create_body import (
    PostPanelApiSettingApiTokensCreateBody,
)
from .post_panel_api_setting_api_tokens_create_response_200 import (
    PostPanelApiSettingApiTokensCreateResponse200,
)
from .post_panel_api_setting_api_tokens_create_response_400 import (
    PostPanelApiSettingApiTokensCreateResponse400,
)
from .post_panel_api_setting_api_tokens_delete_id_body import (
    PostPanelApiSettingApiTokensDeleteIdBody,
)
from .post_panel_api_setting_api_tokens_delete_id_response_200 import (
    PostPanelApiSettingApiTokensDeleteIdResponse200,
)
from .post_panel_api_setting_api_tokens_set_enabled_id_body import (
    PostPanelApiSettingApiTokensSetEnabledIdBody,
)
from .post_panel_api_setting_api_tokens_set_enabled_id_response_200 import (
    PostPanelApiSettingApiTokensSetEnabledIdResponse200,
)
from .post_panel_api_setting_default_settings_response_200 import (
    PostPanelApiSettingDefaultSettingsResponse200,
)
from .post_panel_api_setting_factory_defaults_response_200 import (
    PostPanelApiSettingFactoryDefaultsResponse200,
)
from .post_panel_api_setting_restart_panel_response_200 import (
    PostPanelApiSettingRestartPanelResponse200,
)
from .post_panel_api_setting_test_smtp_response_200 import (
    PostPanelApiSettingTestSmtpResponse200,
)
from .post_panel_api_setting_test_tg_bot_response_200 import (
    PostPanelApiSettingTestTgBotResponse200,
)
from .post_panel_api_setting_update_body import PostPanelApiSettingUpdateBody
from .post_panel_api_setting_update_response_200 import (
    PostPanelApiSettingUpdateResponse200,
)
from .post_panel_api_setting_update_user_body import PostPanelApiSettingUpdateUserBody
from .post_panel_api_setting_update_user_response_200 import (
    PostPanelApiSettingUpdateUserResponse200,
)
from .post_panel_api_setting_validate_regex_response_200 import (
    PostPanelApiSettingValidateRegexResponse200,
)
from .post_panel_api_sub_balancers_id_del_response_200 import (
    PostPanelApiSubBalancersIdDelResponse200,
)
from .post_panel_api_sub_balancers_id_response_200 import (
    PostPanelApiSubBalancersIdResponse200,
)
from .post_panel_api_sub_balancers_response_200 import (
    PostPanelApiSubBalancersResponse200,
)
from .post_panel_api_xray_balancer_override_body import (
    PostPanelApiXrayBalancerOverrideBody,
)
from .post_panel_api_xray_balancer_override_response_200 import (
    PostPanelApiXrayBalancerOverrideResponse200,
)
from .post_panel_api_xray_balancer_status_body import PostPanelApiXrayBalancerStatusBody
from .post_panel_api_xray_balancer_status_response_200 import (
    PostPanelApiXrayBalancerStatusResponse200,
)
from .post_panel_api_xray_geodata_validate_body import (
    PostPanelApiXrayGeodataValidateBody,
)
from .post_panel_api_xray_geodata_validate_response_200 import (
    PostPanelApiXrayGeodataValidateResponse200,
)
from .post_panel_api_xray_nord_action_response_200 import (
    PostPanelApiXrayNordActionResponse200,
)
from .post_panel_api_xray_outbound_subs_id_del_response_200 import (
    PostPanelApiXrayOutboundSubsIdDelResponse200,
)
from .post_panel_api_xray_outbound_subs_id_move_response_200 import (
    PostPanelApiXrayOutboundSubsIdMoveResponse200,
)
from .post_panel_api_xray_outbound_subs_id_refresh_response_200 import (
    PostPanelApiXrayOutboundSubsIdRefreshResponse200,
)
from .post_panel_api_xray_outbound_subs_id_response_200 import (
    PostPanelApiXrayOutboundSubsIdResponse200,
)
from .post_panel_api_xray_outbound_subs_parse_response_200 import (
    PostPanelApiXrayOutboundSubsParseResponse200,
)
from .post_panel_api_xray_outbound_subs_response_200 import (
    PostPanelApiXrayOutboundSubsResponse200,
)
from .post_panel_api_xray_pia_action_response_200 import (
    PostPanelApiXrayPiaActionResponse200,
)
from .post_panel_api_xray_reset_outbounds_traffic_body import (
    PostPanelApiXrayResetOutboundsTrafficBody,
)
from .post_panel_api_xray_reset_outbounds_traffic_response_200 import (
    PostPanelApiXrayResetOutboundsTrafficResponse200,
)
from .post_panel_api_xray_response_200 import PostPanelApiXrayResponse200
from .post_panel_api_xray_route_test_body import PostPanelApiXrayRouteTestBody
from .post_panel_api_xray_route_test_response_200 import (
    PostPanelApiXrayRouteTestResponse200,
)
from .post_panel_api_xray_test_outbound_body import PostPanelApiXrayTestOutboundBody
from .post_panel_api_xray_test_outbound_response_200 import (
    PostPanelApiXrayTestOutboundResponse200,
)
from .post_panel_api_xray_test_outbounds_body import PostPanelApiXrayTestOutboundsBody
from .post_panel_api_xray_test_outbounds_response_200 import (
    PostPanelApiXrayTestOutboundsResponse200,
)
from .post_panel_api_xray_update_response_200 import PostPanelApiXrayUpdateResponse200
from .post_panel_api_xray_warp_action_response_200 import (
    PostPanelApiXrayWarpActionResponse200,
)
from .probe_result_ui import ProbeResultUI
from .reality_scan_result import RealityScanResult
from .server_descendants_item import ServerDescendantsItem
from .server_fail_2_ban_status import ServerFail2BanStatus
from .server_get_new_vless_enc import ServerGetNewVlessEnc
from .server_get_new_vless_enc_auths_item import ServerGetNewVlessEncAuthsItem
from .server_get_new_x25519_cert import ServerGetNewX25519Cert
from .server_get_newmldsa_65 import ServerGetNewmldsa65
from .server_get_newmlkem_768 import ServerGetNewmlkem768
from .server_get_web_cert_files import ServerGetWebCertFiles
from .server_history_item import ServerHistoryItem
from .server_logs_request import ServerLogsRequest
from .server_settings import ServerSettings
from .server_status import ServerStatus
from .server_status_disk import ServerStatusDisk
from .server_status_load import ServerStatusLoad
from .server_status_mem import ServerStatusMem
from .server_status_net_io import ServerStatusNetIO
from .server_status_swap import ServerStatusSwap
from .server_status_xray import ServerStatusXray
from .server_update_panel import ServerUpdatePanel
from .setting import Setting
from .setting_api_tokens_item import SettingApiTokensItem
from .setting_validate_regex_request import SettingValidateRegexRequest
from .sub_balancer import SubBalancer
from .sub_balancer_strategy import SubBalancerStrategy
from .user import User
from .xray import Xray

__all__ = (
    "AllSetting",
    "AllSettingView",
    "AmneziaWGLogs",
    "ApiToken",
    "ApiTokenView",
    "Client",
    "ClientAllowedIPsByInbound",
    "ClientInbound",
    "ClientRecord",
    "ClientReverse",
    "ClientTraffic",
    "ClientTrafficReset",
    "ClientsActiveInbounds",
    "ClientsAddRequest",
    "ClientsAddRequestClient",
    "ClientsAttachRequest",
    "ClientsBulkAdjust",
    "ClientsBulkAdjustRequest",
    "ClientsBulkAdjustSkippedItem",
    "ClientsBulkAttach",
    "ClientsBulkAttachRequest",
    "ClientsBulkCreate",
    "ClientsBulkCreateSkippedItem",
    "ClientsBulkDel",
    "ClientsBulkDelRequest",
    "ClientsBulkDelSkippedItem",
    "ClientsBulkDetach",
    "ClientsBulkDetachRequest",
    "ClientsBulkDisable",
    "ClientsBulkDisableRequest",
    "ClientsBulkDisableSkippedItem",
    "ClientsBulkEnable",
    "ClientsBulkEnableRequest",
    "ClientsBulkEnableSkippedItem",
    "ClientsBulkResetTraffic",
    "ClientsBulkResetTrafficRequest",
    "ClientsClientIpsByGuid",
    "ClientsClientIpsByGuidA1B2",
    "ClientsClientIpsByGuidA1B2User1Item",
    "ClientsDelDepleted",
    "ClientsDelOrphans",
    "ClientsDetachRequest",
    "ClientsExportItem",
    "ClientsExportItemClient",
    "ClientsGroupsBulkAdd",
    "ClientsGroupsBulkAddRequest",
    "ClientsGroupsBulkRemove",
    "ClientsGroupsBulkRemoveRequest",
    "ClientsGroupsCreate",
    "ClientsGroupsCreateRequest",
    "ClientsGroupsDelete",
    "ClientsGroupsDeleteRequest",
    "ClientsGroupsItem",
    "ClientsGroupsRename",
    "ClientsGroupsRenameRequest",
    "ClientsGroupsResetTraffic",
    "ClientsGroupsResetTrafficRequest",
    "ClientsHwidsItem",
    "ClientsImport",
    "ClientsImportRequest",
    "ClientsImportSkippedItem",
    "ClientsLastOnline",
    "ClientsListItem",
    "ClientsListItemTraffic",
    "ClientsListPaged",
    "ClientsListPagedItemsItem",
    "ClientsListPagedItemsItemTraffic",
    "ClientsListPagedSummary",
    "ClientsOnlinesByGuid",
    "ClientsUpdateRequest",
    "ClientsUpdateTrafficRequest",
    "DeletePanelApiClientsHwidsEmailIdResponse200",
    "DeletePanelApiClientsHwidsEmailResponse200",
    "DeletePanelApiSubBalancersIdResponse200",
    "DeletePanelApiXrayOutboundSubsIdResponse200",
    "FallbackParentInfo",
    "GeoCategory",
    "GeoCategoryPage",
    "GeoEntry",
    "GeoEntryPage",
    "GeoFile",
    "GeodataTokenIssue",
    "GetClashPathSubidResponse200",
    "GetCsrfTokenResponse200",
    "GetJsonPathSubidResponse200",
    "GetPanelApiClientsExportResponse200",
    "GetPanelApiClientsGetEmailResponse200",
    "GetPanelApiClientsGetTgIdTgIdResponse200",
    "GetPanelApiClientsGroupsNameEmailsResponse200",
    "GetPanelApiClientsGroupsResponse200",
    "GetPanelApiClientsLinksEmailResponse200",
    "GetPanelApiClientsListPagedResponse200",
    "GetPanelApiClientsListResponse200",
    "GetPanelApiClientsSubLinksSubIdResponse200",
    "GetPanelApiClientsTrafficEmailResponse200",
    "GetPanelApiHostsByInboundInboundIdResponse200",
    "GetPanelApiHostsGetGroupIdResponse200",
    "GetPanelApiHostsListResponse200",
    "GetPanelApiHostsTagsResponse200",
    "GetPanelApiInboundsAllLinksResponse200",
    "GetPanelApiInboundsGetIdResponse200",
    "GetPanelApiInboundsIdFallbacksResponse200",
    "GetPanelApiInboundsListResponse200",
    "GetPanelApiInboundsListSlimResponse200",
    "GetPanelApiInboundsOptionsResponse200",
    "GetPanelApiNodesGetIdResponse200",
    "GetPanelApiNodesHistoryIdMetricBucketResponse200",
    "GetPanelApiNodesListResponse200",
    "GetPanelApiNodesWebCertIdResponse200",
    "GetPanelApiOpenapiJsonResponse200",
    "GetPanelApiServerClientIpsResponse200",
    "GetPanelApiServerCpuHistoryBucketResponse200",
    "GetPanelApiServerDescendantsResponse200",
    "GetPanelApiServerFail2BanStatusResponse200",
    "GetPanelApiServerGetConfigJsonResponse200",
    "GetPanelApiServerGetDbResponse200",
    "GetPanelApiServerGetMigrationResponse200",
    "GetPanelApiServerGetNewUUIDResponse200",
    "GetPanelApiServerGetNewVlessEncResponse200",
    "GetPanelApiServerGetNewX25519CertResponse200",
    "GetPanelApiServerGetNewmldsa65Response200",
    "GetPanelApiServerGetNewmlkem768Response200",
    "GetPanelApiServerGetPanelUpdateInfoResponse200",
    "GetPanelApiServerGetUpdateStatusResponse200",
    "GetPanelApiServerGetWebCertFilesResponse200",
    "GetPanelApiServerGetXrayVersionResponse200",
    "GetPanelApiServerHistoryMetricBucketResponse200",
    "GetPanelApiServerStatusResponse200",
    "GetPanelApiServerXrayMetricsHistoryMetricBucketResponse200",
    "GetPanelApiServerXrayMetricsStateResponse200",
    "GetPanelApiServerXrayObservatoryHistoryTagBucketResponse200",
    "GetPanelApiServerXrayObservatoryResponse200",
    "GetPanelApiSettingApiTokensResponse200",
    "GetPanelApiSettingGetDefaultJsonConfigResponse200",
    "GetPanelApiSubBalancersResponse200",
    "GetPanelApiXrayGeodataCategoriesResponse200",
    "GetPanelApiXrayGeodataEntriesResponse200",
    "GetPanelApiXrayGeodataFilesResponse200",
    "GetPanelApiXrayGetDefaultJsonConfigResponse200",
    "GetPanelApiXrayGetOutboundsTrafficResponse200",
    "GetPanelApiXrayGetXrayResultResponse200",
    "GetPanelApiXrayOutboundSubsResponse200",
    "GetSubPathSubidResponse200",
    "GetWsResponse200",
    "HistoryOfSeeders",
    "Host",
    "HostGroup",
    "HostGroupMihomoIpVersion",
    "HostGroupSecurity",
    "HostMihomoIpVersion",
    "HostSecurity",
    "HostsAddRequest",
    "HostsBulkAddRequest",
    "HostsBulkDelRequest",
    "HostsBulkSetEnableRequest",
    "HostsReorderRequest",
    "HostsSetEnableRequest",
    "HostsUpdateRequest",
    "Inbound",
    "InboundClientIps",
    "InboundFallback",
    "InboundOption",
    "InboundProtocol",
    "InboundShareAddrStrategy",
    "InboundTrafficReset",
    "InboundsAddRequest",
    "InboundsAddRequestSettings",
    "InboundsAddRequestSettingsClientsItem",
    "InboundsAddRequestSniffing",
    "InboundsAddRequestStreamSettings",
    "InboundsAddRequestStreamSettingsRealitySettings",
    "InboundsBulkDel",
    "InboundsBulkDelRequest",
    "InboundsBulkDelSkippedItem",
    "InboundsDelAllClients",
    "InboundsFallbacksItem",
    "InboundsFallbacksRequest",
    "InboundsFallbacksRequestFallbacksItem",
    "InboundsListSlimItem",
    "InboundsListSlimItemSettings",
    "InboundsListSlimItemSettingsClientsItem",
    "InboundsPushClientTrafficsRequest",
    "InboundsPushClientTrafficsRequestTrafficsItem",
    "InboundsSetEnableRequest",
    "InboundsSubSortIndexRequest",
    "Msg",
    "Node",
    "NodeInboundSyncMode",
    "NodeMutationRequest",
    "NodeMutationRequestInboundSyncMode",
    "NodeMutationRequestScheme",
    "NodeMutationRequestTlsVerifyMode",
    "NodeScheme",
    "NodeTlsVerifyMode",
    "NodeView",
    "NodesAddRequest",
    "NodesCertFingerprintRequest",
    "NodesInboundsItem",
    "NodesInboundsRequest",
    "NodesMtlsCa",
    "NodesMtlsTrustCARequest",
    "NodesSetEnableRequest",
    "NodesTestRequest",
    "NodesUpdatePanelItem",
    "NodesUpdatePanelRequest",
    "NodesUpdateRequest",
    "NodesWebCert",
    "OutboundTraffics",
    "PanelUpdateStatus",
    "PeerActivity",
    "PostGetTwoFactorEnableResponse200",
    "PostLoginBody",
    "PostLoginResponse200",
    "PostLoginResponse400",
    "PostLogoutResponse200",
    "PostPanelApiBackuptotgbotResponse200",
    "PostPanelApiClientsActiveInboundsResponse200",
    "PostPanelApiClientsAddResponse200",
    "PostPanelApiClientsBulkAdjustResponse200",
    "PostPanelApiClientsBulkAttachResponse200",
    "PostPanelApiClientsBulkCreateBodyItem",
    "PostPanelApiClientsBulkCreateBodyItemClient",
    "PostPanelApiClientsBulkCreateResponse200",
    "PostPanelApiClientsBulkDelResponse200",
    "PostPanelApiClientsBulkDetachResponse200",
    "PostPanelApiClientsBulkDisableResponse200",
    "PostPanelApiClientsBulkEnableResponse200",
    "PostPanelApiClientsBulkResetTrafficResponse200",
    "PostPanelApiClientsClearIpsEmailResponse200",
    "PostPanelApiClientsClientIpsByGuidResponse200",
    "PostPanelApiClientsDelDepletedResponse200",
    "PostPanelApiClientsDelEmailResponse200",
    "PostPanelApiClientsDelOrphansResponse200",
    "PostPanelApiClientsEmailAttachResponse200",
    "PostPanelApiClientsEmailDetachResponse200",
    "PostPanelApiClientsEmailExternalLinksBody",
    "PostPanelApiClientsEmailExternalLinksBodyExternalLinksItem",
    "PostPanelApiClientsEmailExternalLinksResponse200",
    "PostPanelApiClientsGroupsBulkAddResponse200",
    "PostPanelApiClientsGroupsBulkRemoveResponse200",
    "PostPanelApiClientsGroupsCreateResponse200",
    "PostPanelApiClientsGroupsDeleteResponse200",
    "PostPanelApiClientsGroupsRenameResponse200",
    "PostPanelApiClientsGroupsResetTrafficResponse200",
    "PostPanelApiClientsHwidsEmailResponse200",
    "PostPanelApiClientsImportResponse200",
    "PostPanelApiClientsIpsEmailResponse200",
    "PostPanelApiClientsLastOnlineResponse200",
    "PostPanelApiClientsOnlinesByGuidResponse200",
    "PostPanelApiClientsOnlinesResponse200",
    "PostPanelApiClientsResetAllTrafficsResponse200",
    "PostPanelApiClientsResetTrafficEmailResponse200",
    "PostPanelApiClientsUpdateEmailResponse200",
    "PostPanelApiClientsUpdateTrafficEmailResponse200",
    "PostPanelApiHostsAddResponse200",
    "PostPanelApiHostsBulkAddResponse200",
    "PostPanelApiHostsBulkDelResponse200",
    "PostPanelApiHostsBulkSetEnableResponse200",
    "PostPanelApiHostsDelGroupIdResponse200",
    "PostPanelApiHostsReorderResponse200",
    "PostPanelApiHostsSetEnableGroupIdResponse200",
    "PostPanelApiHostsUpdateGroupIdResponse200",
    "PostPanelApiInboundsAddResponse200",
    "PostPanelApiInboundsAddResponse400",
    "PostPanelApiInboundsBulkDelResponse200",
    "PostPanelApiInboundsDelIdResponse200",
    "PostPanelApiInboundsIdDelAllClientsResponse200",
    "PostPanelApiInboundsIdFallbacksResponse200",
    "PostPanelApiInboundsIdResetTrafficResponse200",
    "PostPanelApiInboundsIdSubSortIndexResponse200",
    "PostPanelApiInboundsImportResponse200",
    "PostPanelApiInboundsPushClientTrafficsResponse200",
    "PostPanelApiInboundsResetAllTrafficsResponse200",
    "PostPanelApiInboundsSetEnableIdResponse200",
    "PostPanelApiInboundsUpdateIdResponse200",
    "PostPanelApiNodesAddResponse200",
    "PostPanelApiNodesCertFingerprintResponse200",
    "PostPanelApiNodesDelIdResponse200",
    "PostPanelApiNodesInboundsResponse200",
    "PostPanelApiNodesMtlsCaResponse200",
    "PostPanelApiNodesMtlsReloadClientResponse200",
    "PostPanelApiNodesMtlsTrustCAResponse200",
    "PostPanelApiNodesProbeIdResponse200",
    "PostPanelApiNodesSetEnableIdResponse200",
    "PostPanelApiNodesTestResponse200",
    "PostPanelApiNodesUpdateIdResponse200",
    "PostPanelApiNodesUpdatePanelResponse200",
    "PostPanelApiServerAmneziawglogsCountBody",
    "PostPanelApiServerAmneziawglogsCountResponse200",
    "PostPanelApiServerClientIpsResponse200",
    "PostPanelApiServerGetCertHashBody",
    "PostPanelApiServerGetCertHashResponse200",
    "PostPanelApiServerGetNewEchCertBody",
    "PostPanelApiServerGetNewEchCertResponse200",
    "PostPanelApiServerGetRemoteCertHashBody",
    "PostPanelApiServerGetRemoteCertHashResponse200",
    "PostPanelApiServerImportDBResponse200",
    "PostPanelApiServerInstallXrayVersionResponse200",
    "PostPanelApiServerLogsCountResponse200",
    "PostPanelApiServerRestartXrayServiceResponse200",
    "PostPanelApiServerRestartXrayServiceResponse400",
    "PostPanelApiServerScanRealityTargetBody",
    "PostPanelApiServerScanRealityTargetResponse200",
    "PostPanelApiServerScanRealityTargetsBody",
    "PostPanelApiServerScanRealityTargetsResponse200",
    "PostPanelApiServerSetUpdateChannelBody",
    "PostPanelApiServerSetUpdateChannelResponse200",
    "PostPanelApiServerStopXrayServiceResponse200",
    "PostPanelApiServerStopXrayServiceResponse400",
    "PostPanelApiServerUpdateGeofileBody",
    "PostPanelApiServerUpdateGeofileFileNameResponse200",
    "PostPanelApiServerUpdateGeofileResponse200",
    "PostPanelApiServerUpdatePanelResponse200",
    "PostPanelApiServerXraylogsCountBody",
    "PostPanelApiServerXraylogsCountResponse200",
    "PostPanelApiSettingAllResponse200",
    "PostPanelApiSettingApiTokensCreateBody",
    "PostPanelApiSettingApiTokensCreateResponse200",
    "PostPanelApiSettingApiTokensCreateResponse400",
    "PostPanelApiSettingApiTokensDeleteIdBody",
    "PostPanelApiSettingApiTokensDeleteIdResponse200",
    "PostPanelApiSettingApiTokensSetEnabledIdBody",
    "PostPanelApiSettingApiTokensSetEnabledIdResponse200",
    "PostPanelApiSettingDefaultSettingsResponse200",
    "PostPanelApiSettingFactoryDefaultsResponse200",
    "PostPanelApiSettingRestartPanelResponse200",
    "PostPanelApiSettingTestSmtpResponse200",
    "PostPanelApiSettingTestTgBotResponse200",
    "PostPanelApiSettingUpdateBody",
    "PostPanelApiSettingUpdateResponse200",
    "PostPanelApiSettingUpdateUserBody",
    "PostPanelApiSettingUpdateUserResponse200",
    "PostPanelApiSettingValidateRegexResponse200",
    "PostPanelApiSubBalancersIdDelResponse200",
    "PostPanelApiSubBalancersIdResponse200",
    "PostPanelApiSubBalancersResponse200",
    "PostPanelApiXrayBalancerOverrideBody",
    "PostPanelApiXrayBalancerOverrideResponse200",
    "PostPanelApiXrayBalancerStatusBody",
    "PostPanelApiXrayBalancerStatusResponse200",
    "PostPanelApiXrayGeodataValidateBody",
    "PostPanelApiXrayGeodataValidateResponse200",
    "PostPanelApiXrayNordActionResponse200",
    "PostPanelApiXrayOutboundSubsIdDelResponse200",
    "PostPanelApiXrayOutboundSubsIdMoveResponse200",
    "PostPanelApiXrayOutboundSubsIdRefreshResponse200",
    "PostPanelApiXrayOutboundSubsIdResponse200",
    "PostPanelApiXrayOutboundSubsParseResponse200",
    "PostPanelApiXrayOutboundSubsResponse200",
    "PostPanelApiXrayPiaActionResponse200",
    "PostPanelApiXrayResetOutboundsTrafficBody",
    "PostPanelApiXrayResetOutboundsTrafficResponse200",
    "PostPanelApiXrayResponse200",
    "PostPanelApiXrayRouteTestBody",
    "PostPanelApiXrayRouteTestResponse200",
    "PostPanelApiXrayTestOutboundBody",
    "PostPanelApiXrayTestOutboundResponse200",
    "PostPanelApiXrayTestOutboundsBody",
    "PostPanelApiXrayTestOutboundsResponse200",
    "PostPanelApiXrayUpdateResponse200",
    "PostPanelApiXrayWarpActionResponse200",
    "ProbeResultUI",
    "RealityScanResult",
    "ServerDescendantsItem",
    "ServerFail2BanStatus",
    "ServerGetNewVlessEnc",
    "ServerGetNewVlessEncAuthsItem",
    "ServerGetNewX25519Cert",
    "ServerGetNewmldsa65",
    "ServerGetNewmlkem768",
    "ServerGetWebCertFiles",
    "ServerHistoryItem",
    "ServerLogsRequest",
    "ServerSettings",
    "ServerStatus",
    "ServerStatusDisk",
    "ServerStatusLoad",
    "ServerStatusMem",
    "ServerStatusNetIO",
    "ServerStatusSwap",
    "ServerStatusXray",
    "ServerUpdatePanel",
    "Setting",
    "SettingApiTokensItem",
    "SettingValidateRegexRequest",
    "SubBalancer",
    "SubBalancerStrategy",
    "User",
    "Xray",
)
