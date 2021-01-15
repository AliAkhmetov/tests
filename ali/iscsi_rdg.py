import names
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from subprocess import PIPE, Popen



capabilities = {
    "browserName": "firefox",
    "version": "80.0",
    "enableVNC": True,
    "enableVideo": False
}

login = 'ali'
pass0 = 'Bac12345'
#driver = webdriver.Firefox()
driver = webdriver.Remote(
    command_executor="http://192.168.1.73:4444/wd/hub/",
    desired_capabilities=capabilities)
driver.get("http://192.168.2.47/")

# --------------- #
# -----LOGIN----- #
# --------------- #

login1 = driver.find_element_by_xpath(names.login1)
login1.click()
login1.click()
login1.send_keys(login)

pass1 = driver.find_element_by_xpath(names.pass1)
pass1.click()
pass1.click()
pass1.send_keys(pass0)

enter1 = driver.find_element_by_xpath(names.enter1)
enter1.click()

# --------------- #
# ----TARGETS---- #
# --------------- #

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, names.block_access)))
block_access = driver.find_element_by_xpath(names.block_access)
iscsi = driver.find_element_by_xpath(names.iscsi)
block_access.click()
iscsi.click()

wait.until(EC.element_to_be_clickable((By.XPATH, names.create_target)))
create_target = driver.find_element_by_xpath(names.create_target)
create_target.click()

target_name1 = 'targetnameqaz' 
target_name = driver.find_element_by_xpath( names.target_name)
target_name.click()
target_name.send_keys(target_name1)
portals = driver.find_element_by_xpath(names.portals)
portals.click()

confirm_target = driver.find_element_by_xpath(names.confirm_target)
confirm_target.click()

# -------------- #
# ----GROUPS---- #
# -------------- #

wait.until(EC.element_to_be_clickable((By.XPATH, names.groups)))
groups = driver.find_element_by_xpath( names.groups)
groups.click()

wait.until(EC.element_to_be_clickable((By.XPATH, names.create_group)))
create_group = driver.find_element_by_xpath(names.create_group)
create_group.click()

group_name1 = 'groupnameqaz' 
group_name = driver.find_element_by_xpath( names.group_name)
group_name.click()
group_name.send_keys(group_name1)

inits_input1 = 'iqn.1993-08.org.debian:01:60dfab34c9ab'
inits_input = driver.find_element_by_xpath( names.inits_input)
inits_input.click()
inits_input.send_keys(inits_input1)

confirm_group = driver.find_element_by_xpath(names.confirm_group)
confirm_group.click()

# --------------- #
# ----MAPPING---- #
# --------------- #

wait.until(EC.element_to_be_clickable((By.XPATH, names.mapping)))
mapping = driver.find_element_by_xpath( names.mapping)
mapping.click()

wait.until(EC.element_to_be_clickable((By.XPATH, names.create_mapping)))
create_mapping = driver.find_element_by_xpath(names.create_mapping)
create_mapping.click()

wait.until(EC.element_to_be_clickable((By.XPATH, names.select_group)))
select_group = driver.find_element_by_xpath( names.select_group)
select_group.click()

wait.until(EC.element_to_be_clickable((By.XPATH, names.select_lun)))
select_lun = driver.find_element_by_xpath( names.select_lun)
select_lun.click()

wait.until(EC.element_to_be_clickable((By.XPATH, names.confirm_mapping)))
confirm_mapping = driver.find_element_by_xpath(names.confirm_mapping)
confirm_mapping.click()

# --------------- #
# ----mapping---- #
# ----in-host---- #
# --------------- #

def executeCmd(cmd, tout=60):
    proc = Popen(cmd, stdout=PIPE, stderr=None, shell=True, encoding="utf-8")
    out = proc.communicate(timeout=tout)[0]
    proc.wait()    # дождаться выполнения
    res = proc.communicate()  # получить tuple('stdout', 'stderr')
    return print(res[0])

executeCmd('iscsiadm -m discovery -t sendtargets -p 192.168.2.34:3260')
executeCmd('iscsiadm -m node -T iqn.2014-07.ru.aerodisk:targetnameqaz -p 192.168.2.34:3260 -l')
executeCmd('mount /dev/sda /mnt/ddp4')
executeCmd('chmod 777 -R /mnt/ddp4')
executeCmd('cd /mnt/ddp4')
executeCmd('fio --randrepeat=1 --ioengine=libaio --direct=1 --gtod_reduce=1 --name=test --filename=test --bs=4k --iodepth=64 --size=4G --readwrite=randrw --rwmixread=75 --runtime=2400')


# --------------- #
# ----mapping---- #
# ----in-host---- #
# --------------- #

driver.quit()