#install.packages("devtools")
devtools::install_github("dkahle/ggmap", ref = "tidyup")
library(ggmap)
register_google(key = "")


df <- read.csv('./서울특별시 대형마트 위치정보.csv', stringsAsFactors=FALSE)

df_latlon <- mutate_geocode(df, `도로명주소`, source='google')

write.csv(df_latlon, './서울특별시 대형마트 위치정보(위경도).csv')
