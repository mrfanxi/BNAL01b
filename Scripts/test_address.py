import os,sys
sys.path.append(os.getcwd())
from Base.read_yaml import ReadYaml
import allure
import pytest
from Page.page_in import PageIn

def get_data(data_type):
#     return [("Leon","18600001111","山西省","临汾市","尧都区","贡院西街1号","041004")]
#     return [("Leon","18600001111","北京市","北京市","朝阳区","XXXXXX号","010001")]
    arrs=[]
    if data_type == "add":
        for data in ReadYaml("address.yaml").read_yaml().get("add_address").values():
            arrs.append((data.get("name"),data.get("phone"),data.get("sheng"),data.get("shi"),data.get("qu"),
                         data.get("info_address"),data.get("code")))
        return arrs
    elif data_type == "updata":
        for data in ReadYaml("address.yaml").read_yaml().get("updata_address").values():
            arrs.append((data.get("name"),data.get("phone"),data.get("sheng"),data.get("shi"),data.get("qu"),
                         data.get("info_address"),data.get("code")))
        return arrs
def get_data1():
    return [("Leon","18600001111","北京市","北京市","朝阳区","XXXXXX号","010001")]
class TestAddress():
    def setup_class(self):
        # 实例化统一入口类,调用登陆方法
        PageIn().page_get_pagelogin().page_login_and_setting()
        # 获取页面地址对象
        self.address=PageIn().page_get_pageaddress()

    def teardown_class(self):
        # 关闭driver
        self.address.driver.quit()

    # 新增地址方法
    @allure.step("开始新增地址操作")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("name, phone, sheng, shi, qu, info_address, code", get_data("add"))
    def test_address(self, name, phone, sheng, shi, qu, info_address, code):
        # 地址管理
        self.address.page_click_address()
        # 点击新增地址
        self.address.page_click_new_address()
        # 收件人
        self.address.page_input_receipt_name(name)
        # 电话
        self.address.page_input_phone(phone)
        # 点击地址封装
        self.address.page_click_Area_sheng_shi_qu(sheng, shi, qu)
        # 输入详细地址
        self.address.page_input_info(info_address)
        # 输入邮编
        self.address.page_input_post_code(code)
        # 设为默认按钮
        self.address.page_click_default_btn()
        # 点击保存
        self.address.page_click_save()

        try:
            expect_result = name + "  " + phone
            assert expect_result in self.address.page_get_list_name_and_phone()
        except:
            # 截图
            self.address.base_getImage()
            # 打开图片写入报告
            with open("./Image/faild.png", "rb") as f:
                allure.attach("失败原因请附图：", f.read(), allure.attach_type.PNG)
            # 抛出异常
            raise
    # 修改地址方法
    @allure.step("开始修改地址操作")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("name,phone,sheng,shi,qu,info_address,code", get_data("updata"))
    def test_updata_address(self, name, phone, sheng, shi, qu, info_address, code):
        self.address.page_click_edit_btn()
        # 点击修改
        self.address.page_click_list_elements("修改")
        # 输入收件人
        self.address.page_input_receipt_name(name)
        # 收入手机号
        self.address.page_input_phone(phone)
        # 所在地区
        self.address.page_click_Area_sheng_shi_qu(sheng,shi,qu)
        # 详细地址
        self.address.page_input_info(info_address)
        # 邮编
        self.address.page_input_post_code(code)
        # 保存
        self.address.page_click_save()
        # 断言
        try:
            # 拼接 收件+电话 格式："xxx  18600001111"
            expect_result = name + "  " + phone
            assert expect_result in self.address.page_get_list_name_and_phone()
        except:
            # 截图
            self.address.base_getImage()
            # 打开图片 并写入报告
            with open("./Image/faild.png", "rb")as f:
                allure.attach("失败原因请附件图：", f.read(), allure.attach_type.PNG)
            # 将捕获的异常 抛出
            raise

    # 删除地址的方法
    @allure.step("开始删除地址操作")
    @pytest.mark.run(order=3)
    def test_delete_address(self):
        if self.address.page_address_manage_is_exist():
            # 点击地址管理
            self.address.page_click_address_manage()
        # # 点击编辑
        # self.address.page_click_edit_btn()
        # # 点击删除
        # self.address.page_click_list_elements("删除")
        # # 确认删除
        # self.address.page_delete_ok()

        # 删除所有地址
        self.address.page_delete_all_address()
        try:
            # 断言地列表是否还存在地址
            assert self.address.page_get_address_list_is_exist()
        except:
        # 截图
            self.address.base_getImage()
            # 打开图片 并写入报告
            with open("./Image/faild.png", "rb")as f:
                allure.attach("失败原因请附件图：", f.read(), allure.attach_type.PNG)
            # 将捕获的异常 抛出
            raise