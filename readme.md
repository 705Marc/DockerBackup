# Installation
1. Clone the GitHub repo to your Docker server
2. Check the Settings.yml and make changes for your system
3. Run: `sudo systemctl status cron` to check if cron is running
4. Start cron: `sudo systemctl start cron`
5. set the python script to executeable `sudo chmod +x /path/to/your/script.py`
6. open the cron table for your user: `crontab -e`
7. add this line to run the backup every day at 3 o clock `0 3 * * * /path/to/your/scirpt.py`
8. save and check the cronjob `crontab -l`
