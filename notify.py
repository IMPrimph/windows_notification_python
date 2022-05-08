import time

from winotify import Notification, audio


toast = Notification(app_id="Jaswanth", title="Hi There!",
                     msg="Know more about me!", duration="short")

toast.add_actions(label="Click Here!", launch="https://jaswanths.netlify.app/")

toast.set_audio(audio.SMS, loop=False)

toast.show()
