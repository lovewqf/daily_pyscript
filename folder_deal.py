# coding:utf-8
import os,sys
import logging
import time
import pdb
def main(head=None,tail=None):
    file_list = os.walk(folder_path)
    file_exist_flag = False
    for root,dir,files in file_list:
        for file in files:
            file_name = file.split('.',1)[0]
            file_extension = file.split('.',1)[-1]
            if file_name == '':
                if file_extension.endswith(tail):
                    file_exist_flag = True
                    try:
                        with open(os.path.abspath(root+os.path.sep+'.'+file_extension),'w') as f:
                            print('%s目录下的 %s File processed successfully' %(root,('.'+file_extension)))
                            logging.info('%s目录下的 %s File processed successfully' %(root,('.'+file_extension)))
                    except Exception as e:
                        print(e)
                        print('%s File processed failed' % ('.' + file_extension))
                        logging.info('%s File processed failed' % ('.' + file_extension))
            if file_name.startswith(head) and file_name.endswith(tail):
                file_exist_flag = True
                if file_name != file_extension:
                    try:
                        with open(os.path.abspath(root+os.path.sep+file_name+'.'+file_extension),'w') as f:
                            print('%s目录下的 %s File processed successfully' %(root,(file_name+'.'+file_extension)))
                            logging.info('%s目录下的 %s File processed successfully' %(root,(file_name+'.'+file_extension)))
                    except Exception as e:
                        print(e)
                        print('%s File processed failed' % (file_name + '.' + file_extension))
                        logging.info('%s File processed failed' % (file_name + '.' + file_extension))
                else:
                    try:
                        with open(os.path.abspath(root+os.path.sep+file_name),'w') as f:
                            print('%s目录下的 %s File processed successfully' %(root,file_name))
                            logging.info('%s目录下的 %s File processed successfully' %(root,file_name))
                    except Exception as e:
                        print(e)
                        print('%s File processed failed' % file_name)
                        logging.error('%s File processed failed' % file_name)
    if file_exist_flag == False:
        print('File start or end argument not found ')
        logging.error('File start or end argument not found ')
        pass
if __name__ == '__main__':
    """
    folder_path: 文件夹的绝对目录
    start：文件名开头提示(若文件名以.开头，则start为.)
    en: 文件名末尾提示
    """
    now_time = time.strftime('%Y_%m_%d',time.localtime())
    logging.basicConfig(filename=r'%s.log'%(now_time),format='%(asctime)s-%(name)s- %(levelname)s-%(message)s',level=logging.INFO)
    try:
        folder_path = sys.argv[1]
        start = sys.argv[2]
        end = sys.argv[3]
    except:
        logging.error('parameter format not correct')
        # raise BaseException('parameter format not correct')
    pdb.set_trace()
    if len(sys.argv) == 4:

        main(start,end)
    else:
        main()