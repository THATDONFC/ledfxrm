"""LedfxrmEntity class"""
from homeassistant.helpers.update_coordinator import CoordinatorEntity
import logging

from custom_components.ledfxrm.const import DOMAIN, NAME, VERSION, MANUFACTURER


class LedfxrmEntity(CoordinatorEntity):
    def __init__(self, coordinator, config_entry):
        super().__init__(coordinator)
        self.config_entry = config_entry
        self.entity_id = "ledfxrm.ledfxrm"

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.entity_id)},
            "name": NAME,
            "model": self.coordinator.data.get("info").get("name") + ' ' + self.coordinator.data.get("info").get("version"),
            "manufacturer": MANUFACTURER,
            "sw_version": VERSION,
        }

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return {
            "time": str(self.coordinator.data.get("time")),
            "static": self.coordinator.data.get("version"),
        }