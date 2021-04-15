# 1st question
1. need to install requests module, to do that run "pip install requests"
2. go into the directory of 1st answer and run "python ans1.py"

# 2nd question
1. need to perform this action first "pip install -r requirements.txt" in ans2 directory
2. create a resource group named try in Azure. Inside it create linux and windows virtual machines.
   az ad sp create-for-rbac -n "trySP" --role Contributor --scopes /subscriptions/{replace with your subscription}/resourceGroups/try
3. This is output something like this
{
  "appId": "............",
  "displayName": "trySP",
  "name": "http://trySP",
  "password": "...................",
  "tenant": "...................."
}
4. take note of appId, password, tenant and add these values in ans2.py along with subscription you used
5. run the python script by going in to the directory of ans2.py
