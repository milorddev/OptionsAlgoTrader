import pathlib
import time
import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

currentDir = pathlib.Path().absolute()

symbols = ['BRK/B','BRX','BSX','BXMT','BYD','BYND','BZH','BZQ','C','CAL','CAT','CCI','CCL','CCMP','CCXX','CF','CGC','CHD','CHGG','CHRW','CHWY','CIEN','CLDR','CLDX','CLF','CLVS','CMCSA','CMG','CNC','CNP','COF','CORN','COST','COTY','CPRI','CRBP','CRDF','CRM','CRON','CSCO','CVM','CVS','CVX','DAL','DDD','DDOG','DE','DG','DGLY','DHI','DHT','DIA','DIS','DKNG','DLR','DLTR','DOCU','DOW','DRD','DVN','DXD','EBAY','EEM','EFA','EFSC','EGO','EMB','ENPH','EOG','EOLS','EPD','ET','ETSY','EUFN','EUO','EVFM','EWZ','EXEL','EXK','F','FB','FBP','FCEL','FCX','FDX','FE','FEAC','FHN','FISV','FLR','FMCI','FOSL','FSLY','FSM','FTAI','FXE','FXI','GAN','GDDY','GDS','GDX','GDXJ','GE','GILD','GIS','GLD','GM','GME','GNUS','GOGO','GOLD','GOOG','GOOGL','GOOS','GRWG','GS','GWRE','HAL','HCAC','HD','HES','HEXO','HL','HPQ','HSBC','HST','HSY','HTH','HTHT','HYG','HZNP','IBB','IBM','IDEX','IFF','IJR','IMAX','IMMU','INO','INTC','IPOB','IQ','ITB','IWM','JBL','JBLU','JD','JDST','JE','JMIA','JNJ','JPM','JWN','KCAC','KGC','KHC','KL','KMI','KMX','KO','KODK','KR','KRE','KSS','KWEB','LAC','LB','LCA','LE','LEN','LEVI','LGND','LIND','LITE','LLY','LPCN','LQD','LTHM','LULU','LUV','LVS','LW','LYFT','M','MA','MAR','MARK','MAXN','MAXR','MBIO','MCD','MDT','MET','MFA','MGM','MIK','MIST','MLCO','MMM','MMYT','MO','MOMO','MOS','MPC','MRK','MRNA','MRO','MS','MSFT','MTCH','MTDR','MTG','MU','MVIS','MYL','NAK','NCLH','NCTY','NEM','NET','NFLX','NGD','NIO','NKE','NKLA','NLOK','NLS','NLY','NMTR','NOK','NUGT','NVDA','NYMT','OC','ODFL','OKTA','OMC','OMI','ON','OPK','OPRA','ORCL','OSTK','OVV','OXY','OZK','PAAS','PBF','PBR','PCG','PE','PEIX','PENN','PEP','PFE','PFSI','PG','PGNY','PINS','PLAY','PLUG','PM','PMT','PNC','PRNB','PRO','PRTY','PRU','PSTG','PSX','PTON','PWR','PXD','PYPL','QCOM','QID','QQQ','QRTEA','QTT','RAD','RCL','RDFN','RDS/A','RIG','RIOT','RKT','RMTI','ROKU','RRR','RTX','RUT','RWM','SABR','SAVA','SAVE','SBSW','SBUX','SCHW','SEAS','SEDG','SFIX','SH','SHAK','SHLL','SILJ','SILV','SIVB','SIX','SKT','SKX','SLB','SLG','SLV','SNAP','SNOW','SO','SOLO','SOYB','SPAQ','SPCE','SPG','SPH','SPLK','SPPI','SPWR','SPX','SPXS','SPXU','SPY','SQ','SQQQ','SRNE','SRTY','SSNC','SSRM','SSSS','STM','SWBI','SWKS','SWN','T','TAN','TCBI','TCO','TCS','TECK','TELL','TEUM','TEVA','TFC','TGB','TGT','TIF','TJX','TLRY','TLT','TNA','TOL','TQQQ','TREX','TRIP','TRNE','TRV','TRVN','TSLA','TSM','TSN','TTOO','TTWO','TWNK','TWO','TWTR','TXRH','TZA','UA','UAA','UBER','UFS','UNFI','UNG','UNH','UPS','URI','USB','UUP','UVXY','UYG','V','VALE','VBIV','VG','VIAC','VIRT','VIX','VIXM','VIXY','VSH','VST','VSTO','VTR','VUZI','VXRT','VXX','VZ','W','WB','WBA','WDC','WFC','WKHS','WMG','WMGI','WMT','WORK','WPM','WTRH','WVE','WWE','X','XAN','XBI','XLB','XLC','XLE','XLF','XLI','XLK','XLNX','XLP','XLRE','XLU','XLV','XLY','XOM','XOP','XRT','XSP','YELP','YEXT','Z','ZGNX','ZM','ZNGA','ZS','ZUO']

driver = webdriver.Chrome(executable_path='{}\chromedriver'.format(currentDir))
driver.get('https://invest.ameritrade.com/grid/p/login')
driver.implicitly_wait(30)

username = driver.find_element_by_name('tbUsername')
username.clear()
username.send_keys(config.username)

passwd = driver.find_element_by_name('tbPassword')
passwd.clear()
passwd.send_keys(config.password)
passwd.send_keys(Keys.RETURN)

time.sleep(4)

driver.get('https://invest.ameritrade.com/grid/p/site#r=watchlist')

for i in symbols:
    optionListInput = driver.find_elements_by_name('addSymbolTextBox')[0]
    optionListInput.clear()
    optionListInput.send_keys(i)
    optionListInput.send_keys(Keys.RETURN)
    time.sleep(1)
