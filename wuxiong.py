from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import pyautogui
import time

path = webdriver.Chrome("D:/chromedriver")
path.get("http://e3.nctu.edu.tw/NCTU_EASY_E3P/LMS3/login.aspx?ReturnUrl=%2fNCTU_EASY_E3P%2fLMS3%2fenter_course_index.aspx");

acc = path.find_element_by_name("txtLoginId")
acc.clear();
acc.send_keys()#your accout
pwd = path.find_element_by_name("txtLoginPwd")
pwd.clear();
pwd.send_keys()#your password

pwd.send_keys(Keys.RETURN)
#time.sleep(20)
#print(path.page_source)

# time.sleep(10)
# path.get("http://e3.nctu.edu.tw/NCTU_EASY_E3P/LMS3/stu_materials_document_list.aspx");
# print(path.page_source)

time.sleep(1)
wjf = path.find_element_by_id("ctl00_ContentPlaceHolder1_gvCourse_ctl02_lnkCourseName");
wjf.click()

docList = path.find_element_by_id("ctl00_lnkDocuments");
docList.click()
main_window = path.current_window_handle

for i in range(3,11):
	for j in range(0,11):
		#ctl00_ContentPlaceHolder1_dgCourseHandout_ctl03_famlDocument_rpFileList_ctl00_lnkFile
		# s = "ctl00_ContentPlaceHolder1_dgCourseHandout_ctl" + str(i) + "_famlDocument_rpFileList_ctl" + str(j) + "_lnkFile"
		# s = "ctl00_ContentPlaceHolder1_dgCourseHandout_ctl03_famlDocument_rpFileList_ctl00_lnkFile"
		# s = "ctl00_ContentPlaceHolder1_dgCourseHandout_ctl" + str(i) + "_famlDocument_rpFileList_ctl" + str(j) + "_lnkFile"
		s = "ctl00_ContentPlaceHolder1_dgCourseHandout_ctl";
		if i<10 :
			s += '0'
		s += str(i) + "_famlDocument_rpFileList_ctl"
		if j<10 :
			s += '0'
		s += str(j) + "_lnkFile"
		print("s = "+s)
		try:
			now_pdf = path.find_element_by_id(s)
			if now_pdf.is_displayed():
				now_pdf.click()
			print("find " + s)
		except NoSuchElementException:
			print("didnt find " + s)
all_handles = path.window_handles
for now in all_handles:
	if now!=main_window:
		# path.switchTo().windows(now)
		path.switch_to_window(now)
		pyautogui.click(1000,500);
		# print(path)
		# time.sleep(1)
		# ac = ActionChains(path)
		# set_driver()
		# try:
		# 	# s = "ctl00_ContentPlaceHolder1_linkUrl"
		# 	s = '//*[@id="ctl00_ContentPlaceHolder1_linkUrl"]'
		# 	#//*[@id="ctl00_ContentPlaceHolder1_linkUrl"]
		# 	# //*[@id="ctl00_ContentPlaceHolder1_btnUrl"]
		# 	# dl = path.find_element_by_xpath("[@type='button']")
		# 	dl = path.find_element_by_id(s)
		# 	if dl.is_displayed():
		# 		dl.click()
		# 	print("find " + s)
		# except NoSuchElementException:
		# 	print("didnt find " + s)
		path.close()


# ctl00_ContentPlaceHolder1_dgCourseHandout_ctl03_famlDocument_rpFileList_ctl00_lnkFile
# ctl00_ContentPlaceHolder1_dgCourseHandout_ctl03_famlDocument_rpFileList_ctl07_lnkFile
# ctl00_ContentPlaceHolder1_dgCourseHandout_ctl03_famlDocument_rpFileList_ctl05_lnkFile
# ctl00_ContentPlaceHolder1_dgCourseHandout_ctl06_famlDocument_rpFileList_ctl03_lnkFile


# print(path.page_source)
