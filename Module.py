import time
from helpers.modules.BaseModule import BaseModule


class Module(BaseModule):
    current = {}
    wait_in_current = 30

    def motion_detection_event(self, *args, **kwargs):
        info = kwargs.get('device', {}).get('name', 'UNKNOWN')

        if info not in self.current:
            self.notify(self._('Motion detection on %s.') % info)

        self.current[info] = time.time()

    def run(self):
        while self.is_running:
            now = time.time()

            for info, last_time in self.current.copy().items():
                if now - last_time > self.wait_in_current:
                    del(self.current[info])

            time.sleep(1)