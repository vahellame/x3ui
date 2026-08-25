from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="AllSetting")


@_attrs_define
class AllSetting:
    """
    Attributes:
        datepicker (str):
        expire_diff (int):
        external_traffic_inform_enable (bool):
        external_traffic_inform_uri (str):
        ip_limit_allowlist (str):
        ldap_auto_create (bool):
        ldap_auto_delete (bool):
        ldap_base_dn (str):
        ldap_bind_dn (str):
        ldap_default_expiry_days (int):
        ldap_default_limit_ip (int):
        ldap_default_total_gb (int):
        ldap_enable (bool):
        ldap_flag_field (str):
        ldap_host (str):
        ldap_inbound_tags (str):
        ldap_insecure_skip_verify (bool):
        ldap_invert_flag (bool):
        ldap_password (str):
        ldap_port (int):
        ldap_sync_cron (str):
        ldap_truthy_values (str):
        ldap_use_tls (bool):
        ldap_user_attr (str):
        ldap_user_filter (str):
        ldap_vless_field (str):
        outbound_down_threshold (int):
        page_size (int):
        panel_outbound (str):
        remark_template (str):
        restart_xray_on_client_disable (bool):
        session_max_age (int):
        smtp_cpu (int):
        smtp_enable (bool):
        smtp_enabled_events (str):
        smtp_encryption_type (str):
        smtp_from (str):
        smtp_from_name (str):
        smtp_host (str):
        smtp_memory (int):
        smtp_password (str):
        smtp_port (int):
        smtp_to (str):
        smtp_username (str):
        sub_announce (str):
        sub_cert_file (str):
        sub_clash_auto_detect (bool):
        sub_clash_enable (bool):
        sub_clash_enable_routing (bool):
        sub_clash_path (str):
        sub_clash_rules (str):
        sub_clash_uri (str):
        sub_clash_user_agent_regex (str):
        sub_domain (str):
        sub_enable (bool):
        sub_enable_routing (bool):
        sub_encrypt (bool):
        sub_hide_settings (bool):
        sub_incy_enable_routing (bool):
        sub_incy_routing_rules (str):
        sub_json_always_array (bool):
        sub_json_auto_detect (bool):
        sub_json_enable (bool):
        sub_json_final_mask (str):
        sub_json_mux (str):
        sub_json_observatory (str):
        sub_json_path (str):
        sub_json_rules (str):
        sub_json_uri (str):
        sub_json_user_agent_regex (str):
        sub_key_file (str):
        sub_listen (str):
        sub_path (str):
        sub_port (int):
        sub_profile_url (str):
        sub_routing_rules (str):
        sub_show_identity_on_all_links (bool):
        sub_support_url (str):
        sub_theme_dir (str):
        sub_title (str):
        sub_uri (str):
        sub_updates (int):
        tg_bot_api_server (str):
        tg_bot_backup (bool):
        tg_bot_chat_id (str):
        tg_bot_enable (bool):
        tg_bot_proxy (str):
        tg_bot_token (str):
        tg_cpu (int):
        tg_enabled_events (str):
        tg_lang (str):
        tg_memory (int):
        tg_run_time (str):
        time_location (str):
        traffic_diff (int):
        trusted_proxy_cid_rs (str):
        two_factor_enable (bool):
        two_factor_token (str):
        warp_update_interval (int):
        web_base_path (str):
        web_cert_file (str):
        web_domain (str):
        web_key_file (str):
        web_listen (str):
        web_port (int):
    """

    datepicker: str
    expire_diff: int
    external_traffic_inform_enable: bool
    external_traffic_inform_uri: str
    ip_limit_allowlist: str
    ldap_auto_create: bool
    ldap_auto_delete: bool
    ldap_base_dn: str
    ldap_bind_dn: str
    ldap_default_expiry_days: int
    ldap_default_limit_ip: int
    ldap_default_total_gb: int
    ldap_enable: bool
    ldap_flag_field: str
    ldap_host: str
    ldap_inbound_tags: str
    ldap_insecure_skip_verify: bool
    ldap_invert_flag: bool
    ldap_password: str
    ldap_port: int
    ldap_sync_cron: str
    ldap_truthy_values: str
    ldap_use_tls: bool
    ldap_user_attr: str
    ldap_user_filter: str
    ldap_vless_field: str
    outbound_down_threshold: int
    page_size: int
    panel_outbound: str
    remark_template: str
    restart_xray_on_client_disable: bool
    session_max_age: int
    smtp_cpu: int
    smtp_enable: bool
    smtp_enabled_events: str
    smtp_encryption_type: str
    smtp_from: str
    smtp_from_name: str
    smtp_host: str
    smtp_memory: int
    smtp_password: str
    smtp_port: int
    smtp_to: str
    smtp_username: str
    sub_announce: str
    sub_cert_file: str
    sub_clash_auto_detect: bool
    sub_clash_enable: bool
    sub_clash_enable_routing: bool
    sub_clash_path: str
    sub_clash_rules: str
    sub_clash_uri: str
    sub_clash_user_agent_regex: str
    sub_domain: str
    sub_enable: bool
    sub_enable_routing: bool
    sub_encrypt: bool
    sub_hide_settings: bool
    sub_incy_enable_routing: bool
    sub_incy_routing_rules: str
    sub_json_always_array: bool
    sub_json_auto_detect: bool
    sub_json_enable: bool
    sub_json_final_mask: str
    sub_json_mux: str
    sub_json_observatory: str
    sub_json_path: str
    sub_json_rules: str
    sub_json_uri: str
    sub_json_user_agent_regex: str
    sub_key_file: str
    sub_listen: str
    sub_path: str
    sub_port: int
    sub_profile_url: str
    sub_routing_rules: str
    sub_show_identity_on_all_links: bool
    sub_support_url: str
    sub_theme_dir: str
    sub_title: str
    sub_uri: str
    sub_updates: int
    tg_bot_api_server: str
    tg_bot_backup: bool
    tg_bot_chat_id: str
    tg_bot_enable: bool
    tg_bot_proxy: str
    tg_bot_token: str
    tg_cpu: int
    tg_enabled_events: str
    tg_lang: str
    tg_memory: int
    tg_run_time: str
    time_location: str
    traffic_diff: int
    trusted_proxy_cid_rs: str
    two_factor_enable: bool
    two_factor_token: str
    warp_update_interval: int
    web_base_path: str
    web_cert_file: str
    web_domain: str
    web_key_file: str
    web_listen: str
    web_port: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datepicker = self.datepicker

        expire_diff = self.expire_diff

        external_traffic_inform_enable = self.external_traffic_inform_enable

        external_traffic_inform_uri = self.external_traffic_inform_uri

        ip_limit_allowlist = self.ip_limit_allowlist

        ldap_auto_create = self.ldap_auto_create

        ldap_auto_delete = self.ldap_auto_delete

        ldap_base_dn = self.ldap_base_dn

        ldap_bind_dn = self.ldap_bind_dn

        ldap_default_expiry_days = self.ldap_default_expiry_days

        ldap_default_limit_ip = self.ldap_default_limit_ip

        ldap_default_total_gb = self.ldap_default_total_gb

        ldap_enable = self.ldap_enable

        ldap_flag_field = self.ldap_flag_field

        ldap_host = self.ldap_host

        ldap_inbound_tags = self.ldap_inbound_tags

        ldap_insecure_skip_verify = self.ldap_insecure_skip_verify

        ldap_invert_flag = self.ldap_invert_flag

        ldap_password = self.ldap_password

        ldap_port = self.ldap_port

        ldap_sync_cron = self.ldap_sync_cron

        ldap_truthy_values = self.ldap_truthy_values

        ldap_use_tls = self.ldap_use_tls

        ldap_user_attr = self.ldap_user_attr

        ldap_user_filter = self.ldap_user_filter

        ldap_vless_field = self.ldap_vless_field

        outbound_down_threshold = self.outbound_down_threshold

        page_size = self.page_size

        panel_outbound = self.panel_outbound

        remark_template = self.remark_template

        restart_xray_on_client_disable = self.restart_xray_on_client_disable

        session_max_age = self.session_max_age

        smtp_cpu = self.smtp_cpu

        smtp_enable = self.smtp_enable

        smtp_enabled_events = self.smtp_enabled_events

        smtp_encryption_type = self.smtp_encryption_type

        smtp_from = self.smtp_from

        smtp_from_name = self.smtp_from_name

        smtp_host = self.smtp_host

        smtp_memory = self.smtp_memory

        smtp_password = self.smtp_password

        smtp_port = self.smtp_port

        smtp_to = self.smtp_to

        smtp_username = self.smtp_username

        sub_announce = self.sub_announce

        sub_cert_file = self.sub_cert_file

        sub_clash_auto_detect = self.sub_clash_auto_detect

        sub_clash_enable = self.sub_clash_enable

        sub_clash_enable_routing = self.sub_clash_enable_routing

        sub_clash_path = self.sub_clash_path

        sub_clash_rules = self.sub_clash_rules

        sub_clash_uri = self.sub_clash_uri

        sub_clash_user_agent_regex = self.sub_clash_user_agent_regex

        sub_domain = self.sub_domain

        sub_enable = self.sub_enable

        sub_enable_routing = self.sub_enable_routing

        sub_encrypt = self.sub_encrypt

        sub_hide_settings = self.sub_hide_settings

        sub_incy_enable_routing = self.sub_incy_enable_routing

        sub_incy_routing_rules = self.sub_incy_routing_rules

        sub_json_always_array = self.sub_json_always_array

        sub_json_auto_detect = self.sub_json_auto_detect

        sub_json_enable = self.sub_json_enable

        sub_json_final_mask = self.sub_json_final_mask

        sub_json_mux = self.sub_json_mux

        sub_json_observatory = self.sub_json_observatory

        sub_json_path = self.sub_json_path

        sub_json_rules = self.sub_json_rules

        sub_json_uri = self.sub_json_uri

        sub_json_user_agent_regex = self.sub_json_user_agent_regex

        sub_key_file = self.sub_key_file

        sub_listen = self.sub_listen

        sub_path = self.sub_path

        sub_port = self.sub_port

        sub_profile_url = self.sub_profile_url

        sub_routing_rules = self.sub_routing_rules

        sub_show_identity_on_all_links = self.sub_show_identity_on_all_links

        sub_support_url = self.sub_support_url

        sub_theme_dir = self.sub_theme_dir

        sub_title = self.sub_title

        sub_uri = self.sub_uri

        sub_updates = self.sub_updates

        tg_bot_api_server = self.tg_bot_api_server

        tg_bot_backup = self.tg_bot_backup

        tg_bot_chat_id = self.tg_bot_chat_id

        tg_bot_enable = self.tg_bot_enable

        tg_bot_proxy = self.tg_bot_proxy

        tg_bot_token = self.tg_bot_token

        tg_cpu = self.tg_cpu

        tg_enabled_events = self.tg_enabled_events

        tg_lang = self.tg_lang

        tg_memory = self.tg_memory

        tg_run_time = self.tg_run_time

        time_location = self.time_location

        traffic_diff = self.traffic_diff

        trusted_proxy_cid_rs = self.trusted_proxy_cid_rs

        two_factor_enable = self.two_factor_enable

        two_factor_token = self.two_factor_token

        warp_update_interval = self.warp_update_interval

        web_base_path = self.web_base_path

        web_cert_file = self.web_cert_file

        web_domain = self.web_domain

        web_key_file = self.web_key_file

        web_listen = self.web_listen

        web_port = self.web_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datepicker": datepicker,
                "expireDiff": expire_diff,
                "externalTrafficInformEnable": external_traffic_inform_enable,
                "externalTrafficInformURI": external_traffic_inform_uri,
                "ipLimitAllowlist": ip_limit_allowlist,
                "ldapAutoCreate": ldap_auto_create,
                "ldapAutoDelete": ldap_auto_delete,
                "ldapBaseDN": ldap_base_dn,
                "ldapBindDN": ldap_bind_dn,
                "ldapDefaultExpiryDays": ldap_default_expiry_days,
                "ldapDefaultLimitIP": ldap_default_limit_ip,
                "ldapDefaultTotalGB": ldap_default_total_gb,
                "ldapEnable": ldap_enable,
                "ldapFlagField": ldap_flag_field,
                "ldapHost": ldap_host,
                "ldapInboundTags": ldap_inbound_tags,
                "ldapInsecureSkipVerify": ldap_insecure_skip_verify,
                "ldapInvertFlag": ldap_invert_flag,
                "ldapPassword": ldap_password,
                "ldapPort": ldap_port,
                "ldapSyncCron": ldap_sync_cron,
                "ldapTruthyValues": ldap_truthy_values,
                "ldapUseTLS": ldap_use_tls,
                "ldapUserAttr": ldap_user_attr,
                "ldapUserFilter": ldap_user_filter,
                "ldapVlessField": ldap_vless_field,
                "outboundDownThreshold": outbound_down_threshold,
                "pageSize": page_size,
                "panelOutbound": panel_outbound,
                "remarkTemplate": remark_template,
                "restartXrayOnClientDisable": restart_xray_on_client_disable,
                "sessionMaxAge": session_max_age,
                "smtpCpu": smtp_cpu,
                "smtpEnable": smtp_enable,
                "smtpEnabledEvents": smtp_enabled_events,
                "smtpEncryptionType": smtp_encryption_type,
                "smtpFrom": smtp_from,
                "smtpFromName": smtp_from_name,
                "smtpHost": smtp_host,
                "smtpMemory": smtp_memory,
                "smtpPassword": smtp_password,
                "smtpPort": smtp_port,
                "smtpTo": smtp_to,
                "smtpUsername": smtp_username,
                "subAnnounce": sub_announce,
                "subCertFile": sub_cert_file,
                "subClashAutoDetect": sub_clash_auto_detect,
                "subClashEnable": sub_clash_enable,
                "subClashEnableRouting": sub_clash_enable_routing,
                "subClashPath": sub_clash_path,
                "subClashRules": sub_clash_rules,
                "subClashURI": sub_clash_uri,
                "subClashUserAgentRegex": sub_clash_user_agent_regex,
                "subDomain": sub_domain,
                "subEnable": sub_enable,
                "subEnableRouting": sub_enable_routing,
                "subEncrypt": sub_encrypt,
                "subHideSettings": sub_hide_settings,
                "subIncyEnableRouting": sub_incy_enable_routing,
                "subIncyRoutingRules": sub_incy_routing_rules,
                "subJsonAlwaysArray": sub_json_always_array,
                "subJsonAutoDetect": sub_json_auto_detect,
                "subJsonEnable": sub_json_enable,
                "subJsonFinalMask": sub_json_final_mask,
                "subJsonMux": sub_json_mux,
                "subJsonObservatory": sub_json_observatory,
                "subJsonPath": sub_json_path,
                "subJsonRules": sub_json_rules,
                "subJsonURI": sub_json_uri,
                "subJsonUserAgentRegex": sub_json_user_agent_regex,
                "subKeyFile": sub_key_file,
                "subListen": sub_listen,
                "subPath": sub_path,
                "subPort": sub_port,
                "subProfileUrl": sub_profile_url,
                "subRoutingRules": sub_routing_rules,
                "subShowIdentityOnAllLinks": sub_show_identity_on_all_links,
                "subSupportUrl": sub_support_url,
                "subThemeDir": sub_theme_dir,
                "subTitle": sub_title,
                "subURI": sub_uri,
                "subUpdates": sub_updates,
                "tgBotAPIServer": tg_bot_api_server,
                "tgBotBackup": tg_bot_backup,
                "tgBotChatId": tg_bot_chat_id,
                "tgBotEnable": tg_bot_enable,
                "tgBotProxy": tg_bot_proxy,
                "tgBotToken": tg_bot_token,
                "tgCpu": tg_cpu,
                "tgEnabledEvents": tg_enabled_events,
                "tgLang": tg_lang,
                "tgMemory": tg_memory,
                "tgRunTime": tg_run_time,
                "timeLocation": time_location,
                "trafficDiff": traffic_diff,
                "trustedProxyCIDRs": trusted_proxy_cid_rs,
                "twoFactorEnable": two_factor_enable,
                "twoFactorToken": two_factor_token,
                "warpUpdateInterval": warp_update_interval,
                "webBasePath": web_base_path,
                "webCertFile": web_cert_file,
                "webDomain": web_domain,
                "webKeyFile": web_key_file,
                "webListen": web_listen,
                "webPort": web_port,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        datepicker = d.pop("datepicker")

        expire_diff = d.pop("expireDiff")

        external_traffic_inform_enable = d.pop("externalTrafficInformEnable")

        external_traffic_inform_uri = d.pop("externalTrafficInformURI")

        ip_limit_allowlist = d.pop("ipLimitAllowlist")

        ldap_auto_create = d.pop("ldapAutoCreate")

        ldap_auto_delete = d.pop("ldapAutoDelete")

        ldap_base_dn = d.pop("ldapBaseDN")

        ldap_bind_dn = d.pop("ldapBindDN")

        ldap_default_expiry_days = d.pop("ldapDefaultExpiryDays")

        ldap_default_limit_ip = d.pop("ldapDefaultLimitIP")

        ldap_default_total_gb = d.pop("ldapDefaultTotalGB")

        ldap_enable = d.pop("ldapEnable")

        ldap_flag_field = d.pop("ldapFlagField")

        ldap_host = d.pop("ldapHost")

        ldap_inbound_tags = d.pop("ldapInboundTags")

        ldap_insecure_skip_verify = d.pop("ldapInsecureSkipVerify")

        ldap_invert_flag = d.pop("ldapInvertFlag")

        ldap_password = d.pop("ldapPassword")

        ldap_port = d.pop("ldapPort")

        ldap_sync_cron = d.pop("ldapSyncCron")

        ldap_truthy_values = d.pop("ldapTruthyValues")

        ldap_use_tls = d.pop("ldapUseTLS")

        ldap_user_attr = d.pop("ldapUserAttr")

        ldap_user_filter = d.pop("ldapUserFilter")

        ldap_vless_field = d.pop("ldapVlessField")

        outbound_down_threshold = d.pop("outboundDownThreshold")

        page_size = d.pop("pageSize")

        panel_outbound = d.pop("panelOutbound")

        remark_template = d.pop("remarkTemplate")

        restart_xray_on_client_disable = d.pop("restartXrayOnClientDisable")

        session_max_age = d.pop("sessionMaxAge")

        smtp_cpu = d.pop("smtpCpu")

        smtp_enable = d.pop("smtpEnable")

        smtp_enabled_events = d.pop("smtpEnabledEvents")

        smtp_encryption_type = d.pop("smtpEncryptionType")

        smtp_from = d.pop("smtpFrom")

        smtp_from_name = d.pop("smtpFromName")

        smtp_host = d.pop("smtpHost")

        smtp_memory = d.pop("smtpMemory")

        smtp_password = d.pop("smtpPassword")

        smtp_port = d.pop("smtpPort")

        smtp_to = d.pop("smtpTo")

        smtp_username = d.pop("smtpUsername")

        sub_announce = d.pop("subAnnounce")

        sub_cert_file = d.pop("subCertFile")

        sub_clash_auto_detect = d.pop("subClashAutoDetect")

        sub_clash_enable = d.pop("subClashEnable")

        sub_clash_enable_routing = d.pop("subClashEnableRouting")

        sub_clash_path = d.pop("subClashPath")

        sub_clash_rules = d.pop("subClashRules")

        sub_clash_uri = d.pop("subClashURI")

        sub_clash_user_agent_regex = d.pop("subClashUserAgentRegex")

        sub_domain = d.pop("subDomain")

        sub_enable = d.pop("subEnable")

        sub_enable_routing = d.pop("subEnableRouting")

        sub_encrypt = d.pop("subEncrypt")

        sub_hide_settings = d.pop("subHideSettings")

        sub_incy_enable_routing = d.pop("subIncyEnableRouting")

        sub_incy_routing_rules = d.pop("subIncyRoutingRules")

        sub_json_always_array = d.pop("subJsonAlwaysArray")

        sub_json_auto_detect = d.pop("subJsonAutoDetect")

        sub_json_enable = d.pop("subJsonEnable")

        sub_json_final_mask = d.pop("subJsonFinalMask")

        sub_json_mux = d.pop("subJsonMux")

        sub_json_observatory = d.pop("subJsonObservatory")

        sub_json_path = d.pop("subJsonPath")

        sub_json_rules = d.pop("subJsonRules")

        sub_json_uri = d.pop("subJsonURI")

        sub_json_user_agent_regex = d.pop("subJsonUserAgentRegex")

        sub_key_file = d.pop("subKeyFile")

        sub_listen = d.pop("subListen")

        sub_path = d.pop("subPath")

        sub_port = d.pop("subPort")

        sub_profile_url = d.pop("subProfileUrl")

        sub_routing_rules = d.pop("subRoutingRules")

        sub_show_identity_on_all_links = d.pop("subShowIdentityOnAllLinks")

        sub_support_url = d.pop("subSupportUrl")

        sub_theme_dir = d.pop("subThemeDir")

        sub_title = d.pop("subTitle")

        sub_uri = d.pop("subURI")

        sub_updates = d.pop("subUpdates")

        tg_bot_api_server = d.pop("tgBotAPIServer")

        tg_bot_backup = d.pop("tgBotBackup")

        tg_bot_chat_id = d.pop("tgBotChatId")

        tg_bot_enable = d.pop("tgBotEnable")

        tg_bot_proxy = d.pop("tgBotProxy")

        tg_bot_token = d.pop("tgBotToken")

        tg_cpu = d.pop("tgCpu")

        tg_enabled_events = d.pop("tgEnabledEvents")

        tg_lang = d.pop("tgLang")

        tg_memory = d.pop("tgMemory")

        tg_run_time = d.pop("tgRunTime")

        time_location = d.pop("timeLocation")

        traffic_diff = d.pop("trafficDiff")

        trusted_proxy_cid_rs = d.pop("trustedProxyCIDRs")

        two_factor_enable = d.pop("twoFactorEnable")

        two_factor_token = d.pop("twoFactorToken")

        warp_update_interval = d.pop("warpUpdateInterval")

        web_base_path = d.pop("webBasePath")

        web_cert_file = d.pop("webCertFile")

        web_domain = d.pop("webDomain")

        web_key_file = d.pop("webKeyFile")

        web_listen = d.pop("webListen")

        web_port = d.pop("webPort")

        all_setting = cls(
            datepicker=datepicker,
            expire_diff=expire_diff,
            external_traffic_inform_enable=external_traffic_inform_enable,
            external_traffic_inform_uri=external_traffic_inform_uri,
            ip_limit_allowlist=ip_limit_allowlist,
            ldap_auto_create=ldap_auto_create,
            ldap_auto_delete=ldap_auto_delete,
            ldap_base_dn=ldap_base_dn,
            ldap_bind_dn=ldap_bind_dn,
            ldap_default_expiry_days=ldap_default_expiry_days,
            ldap_default_limit_ip=ldap_default_limit_ip,
            ldap_default_total_gb=ldap_default_total_gb,
            ldap_enable=ldap_enable,
            ldap_flag_field=ldap_flag_field,
            ldap_host=ldap_host,
            ldap_inbound_tags=ldap_inbound_tags,
            ldap_insecure_skip_verify=ldap_insecure_skip_verify,
            ldap_invert_flag=ldap_invert_flag,
            ldap_password=ldap_password,
            ldap_port=ldap_port,
            ldap_sync_cron=ldap_sync_cron,
            ldap_truthy_values=ldap_truthy_values,
            ldap_use_tls=ldap_use_tls,
            ldap_user_attr=ldap_user_attr,
            ldap_user_filter=ldap_user_filter,
            ldap_vless_field=ldap_vless_field,
            outbound_down_threshold=outbound_down_threshold,
            page_size=page_size,
            panel_outbound=panel_outbound,
            remark_template=remark_template,
            restart_xray_on_client_disable=restart_xray_on_client_disable,
            session_max_age=session_max_age,
            smtp_cpu=smtp_cpu,
            smtp_enable=smtp_enable,
            smtp_enabled_events=smtp_enabled_events,
            smtp_encryption_type=smtp_encryption_type,
            smtp_from=smtp_from,
            smtp_from_name=smtp_from_name,
            smtp_host=smtp_host,
            smtp_memory=smtp_memory,
            smtp_password=smtp_password,
            smtp_port=smtp_port,
            smtp_to=smtp_to,
            smtp_username=smtp_username,
            sub_announce=sub_announce,
            sub_cert_file=sub_cert_file,
            sub_clash_auto_detect=sub_clash_auto_detect,
            sub_clash_enable=sub_clash_enable,
            sub_clash_enable_routing=sub_clash_enable_routing,
            sub_clash_path=sub_clash_path,
            sub_clash_rules=sub_clash_rules,
            sub_clash_uri=sub_clash_uri,
            sub_clash_user_agent_regex=sub_clash_user_agent_regex,
            sub_domain=sub_domain,
            sub_enable=sub_enable,
            sub_enable_routing=sub_enable_routing,
            sub_encrypt=sub_encrypt,
            sub_hide_settings=sub_hide_settings,
            sub_incy_enable_routing=sub_incy_enable_routing,
            sub_incy_routing_rules=sub_incy_routing_rules,
            sub_json_always_array=sub_json_always_array,
            sub_json_auto_detect=sub_json_auto_detect,
            sub_json_enable=sub_json_enable,
            sub_json_final_mask=sub_json_final_mask,
            sub_json_mux=sub_json_mux,
            sub_json_observatory=sub_json_observatory,
            sub_json_path=sub_json_path,
            sub_json_rules=sub_json_rules,
            sub_json_uri=sub_json_uri,
            sub_json_user_agent_regex=sub_json_user_agent_regex,
            sub_key_file=sub_key_file,
            sub_listen=sub_listen,
            sub_path=sub_path,
            sub_port=sub_port,
            sub_profile_url=sub_profile_url,
            sub_routing_rules=sub_routing_rules,
            sub_show_identity_on_all_links=sub_show_identity_on_all_links,
            sub_support_url=sub_support_url,
            sub_theme_dir=sub_theme_dir,
            sub_title=sub_title,
            sub_uri=sub_uri,
            sub_updates=sub_updates,
            tg_bot_api_server=tg_bot_api_server,
            tg_bot_backup=tg_bot_backup,
            tg_bot_chat_id=tg_bot_chat_id,
            tg_bot_enable=tg_bot_enable,
            tg_bot_proxy=tg_bot_proxy,
            tg_bot_token=tg_bot_token,
            tg_cpu=tg_cpu,
            tg_enabled_events=tg_enabled_events,
            tg_lang=tg_lang,
            tg_memory=tg_memory,
            tg_run_time=tg_run_time,
            time_location=time_location,
            traffic_diff=traffic_diff,
            trusted_proxy_cid_rs=trusted_proxy_cid_rs,
            two_factor_enable=two_factor_enable,
            two_factor_token=two_factor_token,
            warp_update_interval=warp_update_interval,
            web_base_path=web_base_path,
            web_cert_file=web_cert_file,
            web_domain=web_domain,
            web_key_file=web_key_file,
            web_listen=web_listen,
            web_port=web_port,
        )

        all_setting.additional_properties = d
        return all_setting

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
