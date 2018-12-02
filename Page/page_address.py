import Page
from Base.base import Base

class PageAddress(Base):
    # 地址管理
    def page_click_address(self):
        self.base_click(Page.address_manage)
    # 点击新增地址
    def page_click_new_address(self):
        self.base_click(Page.address_add_new_btn)
    # 收件人
    def page_input_receipt_name(self, name):
        self.base_input(Page.address_receipt_name, name)
    # 电话
    def page_input_phone(self, phone):
        self.base_input(Page.address_add_phone, phone)
    # 点击 所在区域
    def page_click_Area(self):
        self.base_click(Page.address_province)
    # 省
    def page_click_sheng(self, sheng):
        self.base_text_click(sheng)
    # 市
    def page_click_shi(self, shi):
        self.base_text_click(shi)
    # 区
    def page_click_qu(self, qu):
        self.base_text_click(qu)

    # 点击地址封装
    def page_click_Area_sheng_shi_qu(self,sheng,shi,qu):
        # 点击所在区域
        self.page_click_Area()
        # 省
        self.page_click_sheng(sheng)
        # 市-非直辖
        # self.page_click_shi(shi)
        # 包裹直辖市的框
        self.base_click(Page.address_zhixiashi_kuang)
        # 直辖市
        self.base_click(Page.address_zhixiashi)
        # 区
        self.page_click_qu(qu)

    # 输入详细地址
    def page_input_info(self, info_address):
        self.base_input(Page.address_detail_addr_info,info_address)
    # 输入邮编
    def page_input_post_code(self, code):
        self.base_input(Page.address_post_code, code)
    # 设为默认按钮
    def page_click_default_btn(self):
        self.base_click(Page.address_default)
    # 点击保存
    def page_click_save(self, text="保存"):
        self.base_text_click(text)

    # 返回地址管理列表 收件人+电话
    def page_get_list_name_and_phone(self):
        # 获取的结果 如：["张三  18611110000","李四  18600002222"]
        return self.base_get_list_text(Page.address_name_and_phone)
    # 点击编辑
    def page_click_edit_btn(self,text="编辑"):
        self.base_text_click(text)
    # 获取所有元素列表，并且点击相应的元素
    def page_click_list_elements(self, text):
        self.base_text_get_elements_and_click(text)