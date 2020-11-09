"""Adds config flow for Ledfxrm."""
from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol
import logging
import requests
from .const import ( 
    CONF_HOST,
    CONF_PORT,
    DOMAIN,
    PLATFORMS,
)

YZNAME = "namea"
YZNAMEB = "nameb"
CONF_HOST = "host"
CONF_PORT = "port"



class LedfxrmFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""

    async def async_step_user(self, info):
        if info is not None:
            logging.warning('BLADE=====> Info: %s', info)
            logging.warning('BLADE=====> Host: %s', info['host'])
            logging.warning('BLADE=====> Port: %s', info['port'])
            try:
                r0 = requests.get("http://" + info['host'] + ':' + info['port'] + "/api/info")
                logging.warning('BLADE=====> API: %s', r0.json())
            except:
                pass  # TODO: process info
        if info is None:
            return self.async_show_form(
                step_id="user", data_schema=vol.Schema({
                    vol.Required(CONF_HOST, default="192.168.1.56"): str,
                    vol.Optional(CONF_PORT, default=8888): int, 
                    vol.Optional(YZNAME, default="check1"): str, 
                    vol.Optional(YZNAMEB, default="check2"): str, 
                })
            )
        return self.async_create_entry(
            title="title",
            data={'CONF_HOST': info['host'], 'CONF_PORT': info['port']},
        )
    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        logging.warning('Get Options!!!')
        return LedfxrmOptionsFlowHandler()
        
        
class LedfxrmOptionsFlowHandler(config_entries.OptionsFlow):
    async def async_step_init(self, user_input=None):
        logging.warning('Manage the options!!!')
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        "CONF_NAME",
                        default=self.config_entry.options.get("CONF_NAME"),
                    ): bool
                }
            ),
        )



# """Adds config flow for Ledfxrm."""
# from homeassistant import config_entries
# from homeassistant.core import callback
# import voluptuous as vol
# import logging
# import requests
# from custom_components.ledfxrm.const import (  # pylint: disable=unused-import
#     CONF_HOST,
#     CONF_PORT,
#     DOMAIN,
#     PLATFORMS,
# )


# class LedfxrmFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
#     """Config flow for Ledfxrm."""

#     VERSION = 1
#     CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

#     def __init__(self):
#         """Initialize."""
#         logging.warning('Config FLOW!!!')
#         self._errors = {}

#     async def async_step_user( self, user_input=None ):
#         """Handle a flow initialized by the user."""
#         self._errors = {}
    
#         if self._async_current_entries():
#             return self.async_abort(reason="single_instance_allowed")

#         if user_input is not None:
#             valid = await self._test_credentials(
#                 user_input[CONF_HOST], user_input[CONF_PORT]
#             )
#             if valid:
#                 return self.async_create_entry(
#                     title=user_input[CONF_HOST], data=user_input
#                 )
#             else:
#                 self._errors["base"] = "auth"

#             return await self._show_config_form(user_input)

#         return await self._show_config_form(user_input)

#     @staticmethod
#     @callback
#     def async_get_options_flow(config_entry):
#         return LedfxrmOptionsFlowHandler(config_entry)

#     async def _show_config_form(self, user_input):  # pylint: disable=unused-argument
#         """Show the configuration form to edit location data."""
#         return self.async_show_form(
#             step_id="user",
#             data_schema=vol.Schema(
#                 {vol.Required(CONF_HOST): str, vol.Required(CONF_PORT): int}
#             ),
#             errors=self._errors,
#         )

#     async def _test_credentials(self, thehost, theport):
#         """Return true if credentials is valid."""
#         try:
#             client = requests.get("http://" + thehost + ":" + theport + "/api/info")
#             await client.async_get_data()
#             return True
#         except Exception:  # pylint: disable=broad-except
#             pass
#         return False


# class LedfxrmOptionsFlowHandler(config_entries.OptionsFlow):
#     """Ledfxrm config flow options handler."""

#     def __init__(self, config_entry):
#         """Initialize HACS options flow."""
#         self.config_entry = config_entry
#         self.options = dict(config_entry.options)

#     async def async_step_init(self, user_input=None):  # pylint: disable=unused-argument
#         """Manage the options."""
#         return await self.async_step_user()

#     async def async_step_user(self, user_input=None):
#         """Handle a flow initialized by the user."""
#         if user_input is not None:
#             self.options.update(user_input)
#             return await self._update_options()

#         return self.async_show_form(
#             step_id="user",
#             data_schema=vol.Schema(
#                 {
#                     vol.Required(x, default=self.options.get(x, True)): bool
#                     for x in sorted(PLATFORMS)
#                 }
#             ),
#         )

#     async def _update_options(self):
#         """Update config entry options."""
#         return self.async_create_entry(
#             title=self.config_entry.data.get(CONF_HOST), data=self.options
#         )
