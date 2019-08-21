"""
    本程序利用了instagram-scraper
    安装请使用pip install instagram-scraper
    请开启全局代理访问ins

    --login-user  -u    Instagram login user.
    --login-pass  -p    Instagram login password.
    --destination -d    Specify the download destination. By default, media will 
                        be downloaded to <current working directory>/<username>.
    --retain-username -n  Creates a username subdirectory when the destination flag is
                        set.
    --media-types -t    Specify media types to scrape. Enter as space separated values. 
                        Valid values are image, video, story (story-image & story-video),
                        or none. Stories require a --login-user and --login-pass to be defined.
    --latest            Scrape only new media since the last scrape. Uses the last modified
                        time of the latest media item in the destination directory to compare.
    --maximum     -m    Maximum number of items to scrape.
    --proxies           Enable use of proxies, add a valid JSON with http or/and https urls.
                        Example: '{"http": "http://<ip>:<port>", "http": "https://<ip>:<port>" }'
    --template -T       Customize and format each file's name.
                        Default: {urlname}
                        Options:
                        {username}: Scraped user
                        {shortcode}: Post shortcode (profile_pic and story are empty)
                        {urlname}: Original file name from url.
                        {datetime}: Date and time of upload. (Format: 20180101 01h01m01s)
                        {date}: Date of upload. (Format: 20180101)
                        {year}: Year of upload. (Format: 2018)
                        {month}: Month of upload. (Format: 01-12)
                        {day}: Day of upload. (Format: 01-31)
                        {h}: Hour of upload. (Format: 00-23h)
                        {m}: Minute of upload. (Format: 00-59m)
                        {s}: Second of upload. (Format: 00-59s)

                        If the template is invalid, it will revert to the default.
                        Does not work with --tag and --location.
"""
import os


def ins_download(_update, _ins_user):
    if _update == 1:
        cmd = 'instagram-scraper ' + ','.join(_ins_user) + ' --latest'
    os.system(cmd)


def __main__():
    my_account = '-u lixplus -p Lidathena10'
    update = 1
    ins_dir = r'D:\MyFiles\Downloads\Pictures\Instagram'
    os.chdir(ins_dir)
    user_list = os.listdir(ins_dir)
    for user in user_list[::]:
        if os.path.isfile(os.path.join(ins_dir, user)):
            user_list.remove(user)
    user_list += ['velyyson_g', 'djamberna', 'yun.jj', 'djjina_official']
    ins_download(update, user_list)


if __name__ == "__main__":
    __main__()
