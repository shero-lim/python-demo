def compare_image_by_opencv(base_file_path, cmp_file_path):
    from skimage.measure import compare_ssim
    import cv2

    try:
        imageA = cv2.imread(base_file_path)
        imageB = cv2.imread(cmp_file_path)
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
        (score, diff_mat) = compare_ssim(grayA, grayB, full=True)
        log_output("compare_image_by_opencv - score:{}".format(score))

    except Exception as e:
        log_output("base_file_path:{}".format(base_file_path))
        log_output("cmp_file_path:{}".format(cmp_file_path))
        log_output("compare_image_by_opencv occurs exception:{}".format(e.message))
        time.sleep(1)
        score = 0

    return score


def download_package(oss_url, oss_save_path):
    import urllib2
    try:
        log_output("下载资源 - oss_url:{}".format(oss_url))
        req = urllib2.urlopen(oss_url)
        data = req.read()
        log_output("下载结束")
    except Exception as e:
        log_output("下载出错:{}".format(e.message))
    else:
        with open(oss_save_path, "wb") as fp:
            fp.write(data)


def unzip_package(so_zip_path):
    so_folder_path = so_zip_path[:-4]

    # 先删除原资源再解压
    if os.path.isdir(so_folder_path):
        log_output("删除原有资源文件:{}".format(so_folder_path))
        shutil.rmtree(so_folder_path)

    try:
        zf = zipfile.ZipFile(so_zip_path)
        zf.extractall(path=so_folder_path)
        zf.close()
        log_output("解压完成，资源路径:{}\n".format(so_folder_path))

    except Exception as e:
        log_output("解压异常:{}".format(e.message))

    os.remove(so_zip_path)
    return so_folder_path


def get_json_content(file_path):
    with open(file_path) as fp:
        params_dict = json.load(fp)
    return params_dict
