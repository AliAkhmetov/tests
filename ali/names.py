# --------------- #
# -----iSCSI----- #
# ------RDG------ #
# --------------- #

login1 = '//*[@id="Login"]/div[1]/input'
pass1 = '//*[@id="Login"]/div[2]/input'
enter1 = '//*[@id="Login"]/button'
block_access = '//span[text()="Блочный доступ"]'
iscsi = '//a[text()="iSCSI"]'

create_target = '//button[text()="Создать таргет"]'
target_name = '//input[@name="target"]'
portals = '//select[@name="portals"]/option[1]'
confirm_target = '//button[text()="Подтвердить"]'

groups = '//a[@data-id="group"]'
create_group = '//button[text()="Создать группу"]'
group_name = '//input[@name="group"]'
inits_input = '//input[@name="inits"]/../div/input[@type="text"]'
confirm_group = '//button[text()="Подтвердить"]'

mapping = '//a[@data-id="mapping"]'
create_mapping = '//button[text()="Создать маппинг"]'
select_group = '//label[text()="Группа:"]/../div/div[2]/div[1]'
select_lun = '//label[text()="Выберите логические тома:"]/../div/div[2]/div[1]'
confirm_mapping = '//button[text()="Подтвердить"]'

# --------------- #
# -----iSCSI----- #
# ------DDP------ #
# --------------- #

# --------------- #
# -Fibre Channel- #
# ------RDG------ #
# --------------- #

# --------------- #
# -Fibre Channel- #
# ------DDP------ #
# --------------- #

