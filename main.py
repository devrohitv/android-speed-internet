from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.app import runTouchApp
from kivy.uix.boxlayout import BoxLayout

from jnius import autoclass
Context = autoclass("android.content.Context")
ConectivityManager = autoclass("android.net.ConnectivityManager")
NetworkCapablities = autoclass("android.net.NetworkCapabilities")

context = Context.getApplicationContext()
conectivitymanager = ConectivityManager()
networkcapablities = NetworkCapablities()

cm = context.getSystemService(Context.CONNECTIVITY_SERVICE)
# nc = cm.getNetworkCapabilities(cm.getActiveNetwork())


class Meter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label()
        self.add_widget(self.label)

        Clock.schedule_interval(self.update_label, 1)

    def update_label(self, dt):
        nc = cm.getNetworkCapabilities(cm.getActiveNetwork())
        if nc:
            downloadSpeed = nc.getLinkDownstreamBandwidthKbps()
            uploadSpeed = nc.getLinkUpstreamBandwidthKbps()
        

        self.label.text = f"Download {str(downloadSpeed)}, Upload {str(uploadSpeed)}"


runTouchApp(Meter())
