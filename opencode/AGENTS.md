# Project Memory

## Rules

### Prohibited
- Never do changes directly using kubectl.
- Never do direct changes using gcloud cli.
- When you add changes, never staged your changes unless I told you to do that.
- Never restore the changes in staged, unless I told you to do that.

### Must do
- to reduce cost, always use gke-spot or any better solution in staging environment. but use the regular node in production.
- in production, makes image pullPolicy as IfNotPresent. but in staging, make it as Always.
- When creating PR in folder repositories inside /Users/ibnumuhammad/Documents/ajaib , always add the Jira Ticket number in the PR title like "[DDE-1121] patch flink fiat-ledger-top-up-rdn secret in stg" , you need to adjust the Jira Ticket number of "[DDE-1121]" based on Jira Ticket issue.
- You can check whether the Jira Ticket is already available in Jira project DDE https://ajaib.atlassian.net/jira/software/projects/DDE/boards/37/backlog , check the Jira Ticket using jira mcp, then use the Jira Ticket number in the PR title.
- If the related ticket is not available yet, create the new ticket, assign it to me "Ibnu Muhammad", and put the ticket into the current sprint, then use the Jira Ticket number in the PR title.
- When I ask you to open browser, always open the automation Playwright Browser.
- GSM secret name is using this naming pattern "{BU}__{DB_NAME/PLATFORM_NAME}__{ACCESS_PRIVILEGE}__{SECRET_PROPERTY}"