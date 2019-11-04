import os
import shutil


def copy_debug(force_replace):
    src_debug_lyra = r"E:\iqiyi\pca_infra\publish\lyra\bin\x86\debug\lyra.dll"
    src_debug_lyraui = r"E:\iqiyi\pca_infra\publish\lyraui\bin\x86\release-md-noz\QuiLib.dll"
    src_debug_skia = r"E:\iqiyi\pca_infra\publish\skia\bin\x86\debug\skia.dll"
    src_debug_apppluginbase = r"E:\iqiyi\pca_infra\publish\apppluginbase\bin\x86\release-md-noz\appPluginBase.dll"
    src_folder = [src_debug_lyra, src_debug_lyraui, src_debug_skia, src_debug_apppluginbase]
    dst_folder = r"C:\Program Files (x86)\IQIYI Video\LStyle\7.1.99.1123_test"

    for file_path in src_folder:
        dst_name = dst_folder + "\\" + os.path.basename(file_path)
        if not force_replace:
            if os.path.exists(dst_name):
                continue
        shutil.copy(file_path, dst_folder)


def copy_release(force_replace):
    src_release_lyra = r"E:\iqiyi\pca_infra\publish\lyra\bin\x86\release\lyra.dll"
    src_release_lyraui = r"E:\iqiyi\pca_infra\publish\lyraui\bin\x86\release-md\QuiLib.dll"
    src_release_skia = r"E:\iqiyi\pca_infra\publish\skia\bin\x86\release\skia.dll"
    src_folder = [src_release_lyra, src_release_lyraui, src_release_skia]
    dst_folder = r"C:\Program Files (x86)\IQIYI Video\LStyle\7.1.100.1170"
    for file_path in src_folder:
        dst_name = dst_folder + "\\" + os.path.basename(file_path)
        if not force_replace:
            if os.path.exists(dst_name):
                continue
        shutil.copy(file_path, dst_folder)

if __name__ == '__main__':
    # copy_debug(True)
    copy_release(True)
