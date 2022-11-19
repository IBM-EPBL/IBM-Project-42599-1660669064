import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME= 3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31498;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=wll19778;PWD=Lan4GFP8i1ksQEFG",'','')
print(conn)
print("connection successful...")