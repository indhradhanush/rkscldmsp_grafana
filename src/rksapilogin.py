# Ruckus Cloud MSP - Python program to extract from API and update influx database.

# rksapilogin.py - Retrieves password from keyring and log into Ruckus Cloud. Fetches API-KEY.
# - Store password in operating system keyring securely. Avoid storing password in text readable format.


from configure import *
# pip install keyring
import keyring

cred = keyring.get_credential(rks_domain, rks_username)
rks_password=cred.password

def apilogin(session):
    # Obtain authentication cookie (cookie is saved to the session)
    print('Logging in to: https://', rks_domain)
    resp = session.post('https://' + rks_domain + '/token', json={'username': rks_username, 'password': rks_password})
    respjson = resp.json()
    if resp.status_code == 200:
        tid=respjson['tenantId']
        print('Tenant:', tid)
        print('API-KEY:', resp.json()['API-KEY'])
        return tid
    else:
        print("Login failed")
        exit()
