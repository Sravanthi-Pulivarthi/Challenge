The Azure Instance Metadata Service (IMDS) provides information about currently running virtual machine instances. You can use it to manage and configure your virtual machines. This information includes the SKU, storage, network configurations, and upcoming maintenance events. For a complete list of the data available, see the Endpoint Categories Summary.

IMDS is a REST API that's available at a well-known, non-routable IP address (169.254.169.254). You can only access it from within the VM. Communication between the VM and IMDS never leaves the host. Have your HTTP clients bypass web proxies within the VM when querying IMDS, and treat 169.254.169.254 the same as 168.63.129.16.

Access Azure Instance Metadata Service

#Raw data

curl -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance?api-version=2021-02-01" | jq 

#Compute only, could do Network, all the main JSON headings

curl -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/compute?api-version=2021-01-01" | jq 

#Just get tags

curl -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/compute/tagsList?api-version=2021-01-01" | jq 

#Scheduled events (this includes things like terminations if VMSS with grace window)

curl -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/scheduledevents?api-version=2019-08-01" | jq 

# To Get user data

curl -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance/compute/userData?api-version=2021-01-01&format=text" | base64 --decode


