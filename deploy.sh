#!/bin/bash
gcloud run jobs deploy modreportbot-modlog --region europe-west1 --project bots-424808 --source . --set-env-vars=LEMMY_USER="charles_petrescu",LEMMY_INSTANCE="feddit.uk",MATRIX_USER="@robot_bunny:matrix.org",MATRIX_SERVER="matrix.org",MATRIX_ROOM="!JvATVaovRwoZeJNnas:beeper.com",GET_REPORTS="TRUE",FLAG_DOWNVOTES="FALSE",GET_MESSAGES="TRUE",NOTIFY_NEW="TRUE",GET_MODLOG="TRUE",MODLOG_PM="TRUE" --set-secrets="LEMMY_PW=charles:latest","MATRIX_PW=robotbunny:latest" &

# add for DMs:
#bedsnewsbot
#quakebot
#tellyaddict
#mrchuffy
#bunny_fairy

wait
