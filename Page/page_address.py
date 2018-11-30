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
    def page_input_receipt_name(self, username):
        self.base_input(Page.address_receipt_name, username)
    # 电话
    def page_input_phone(self, phone):
        self.base_input(Page.address_add_phone, phone)
    # 点击 所在区域
    def page_click_Area(self):
        self.base_click(Page.address_province)
    # 省
    def page_click_sheng(self, sheng):
        self.base_click(sheng)
    # 市
    def page_click_shi(self, shi):
        self.base_click(shi)
    # 区
    def page_click_qu(self, qu):
        self.base_click(qu)
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
        self.base_click(text)