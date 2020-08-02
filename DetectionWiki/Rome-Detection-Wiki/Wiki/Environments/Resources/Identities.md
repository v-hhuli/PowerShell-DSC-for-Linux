This list contains only the subscriptions where our deployment is actually exists and not contains any subscription used for any test scenario

# Identity KeyVault names

| Cloud Environment | Environment | KV Name | AuthorityId | AuthorityName
|-----------|-----------|-----------|-----------|-----------|
Public | Dev | Identity-Dev-CUS | 00000000-0000-0000-0000-000000000001 | AME
Public | Stage | Identity-Stage-CUS | 00000000-0000-0000-0000-000000000001 | AME
Public | Prod | Identity-Prod-CUS | 00000000-0000-0000-0000-000000000001 | AME
Fairfax | Dev | Identity-Dev-VR | 00000000-0000-0000-0000-000000000001 | AME
Fairfax | Stage | Identity-Stage-VR | 00000000-0000-0000-0000-000000000001 | AME
Fairfax | Prod | Identity-Prod-VR | 00000000-0000-0000-0000-000000000001 | AME
Mooncake | Stage | Identity-Stage-ECH2 | 00000000-0000-0000-0000-000000000001 | AME
Mooncake | Prod | Identity-Prod-ECH2 | 00000000-0000-0000-0000-000000000001 | AME
Ex | Prod | Identity-Prod-Red | 00000000-0000-0000-0000-000000000001 | AME
Rx | Prod | Identity-Prod-USSE | 00000000-0000-0000-0000-000000000001 | ussec

# Identities

## Alert Mgmt

| Cloud Environment | Environment | Display name | App ID | Object Id | SPN Object Id | Subject Name
|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
Public | Dev | dev.alertmanagement.detection.rome.azure.com | 8202a28a-0027-48b4-9022-7db85a985558 | 961fb407-a70b-4bf5-9cd5-d6bad19a3c8c | ac81d332-aa81-49a6-8609-9f8ea1cb6591 | dev.alertmanagement.detection.rome.azure.com
Public | Stage | stage.alertmanagement.detection.rome.azure.com | 2c0cff35-5720-4752-b017-9955d4801862 | d5825138-4ae4-4e93-868a-048e9a516557 | AME: 52b8c899-6a39-4ebc-a34c-cf693ee79916, Corp: 80f188c8-cf94-49c5-b25d-63f7a68d3586 | stage.alertmanagement.detection.rome.azure.com
Public | Prod | prod.alertmanagement.detection.rome.azure.com | 4cd2ef57-3441-4a8d-a8dc-c6f7541a8f9a | f2620ef7-739c-454c-946c-bd7941f7b0ac | AME: 34705429-2f72-4132-bd56-3328a9d4b7d8 CORP: 370ef6e0-7903-4f20-ae1b-9cee47b3936f | prod.alertmanagement.detection.rome.azure.com
Fairfax | Dev | dev.alertmanagement.detection.rome.azure.us | b2f8ad0a-4a68-444f-83a1-3c331a7d0f8b | de5d7279-edf7-4ed5-9094-dbe9ad0b8be0 | 32516dda-ce0d-4f8d-be11-d2ae9daf0227 | dev.alertmanagement.detection.rome.azure.us
Fairfax | Stage | stage.alertmanagement.detection.rome.azure.us | ed9a2ac1-1495-45f0-ae38-afbe41eff824 | 230700f3-c349-4eca-9b48-3fb8fbe19b66 | 0e3cf1bc-2dbc-4050-99db-0fb0d42dcfd7 | stage.alertmanagement.detection.rome.azure.us
Fairfax | Prod | prod.alertmanagement.detection.rome.azure.us | 8f97e868-200c-4674-b148-f6492de5129b | ddd9d0b1-fe30-43bb-b9d6-301bf9cb16e5 | 7cc32dbe-81b0-4edc-b420-277e0d7e731e | prod.alertmanagement.detection.rome.azure.us
Mooncake | Stage | alertmanagement.stage.detection.rome.azure.cn | cd96a4bc-1dd0-47c5-be74-0db0f14010d1 | e5b0702c-fbfd-4433-8c1c-eb8d7366c8b7 | 210d6af7-815e-4c68-96b1-45ac010ef11b | stage.alertmanagement.detection.rome.azure.cn
Mooncake | Prod | alertmanagement.prod.detection.rome.azure.cn | 79272c36-6ea8-4b55-bd77-0936a6c09b8f | 5a51e537-3704-49da-bd01-1a0a6c711858 | 1858cecf-356d-4034-837a-9e952549dccd | prod.alertmanagement.detection.rome.azure.cn
EX | Prod | prod.alertmanagement.detection.rome.azure.eaglex.ic.gov | 31b793d4-842f-4f58-9135-61c60a596f33 | 89d27f5c-6b33-4ad9-8e01-cf83fd238792 | b16325bd-03f4-48c0-a010-7ec89cec75d9 | prod.alertmanagement.detection.rome.azure.eaglex.ic.gov
RX | Prod | prod.alertmanagement.detection.rome.azure.microsoft.scloud | bd9a3bac-a70f-4249-a612-17d7dbae473d | ef21c728-8a7e-4384-8821-bea95127b4d0 | d7a44fb6-d45e-4c36-ab94-c45f3236877b | prod.alertmanagement.detection.rome.azure.microsoft.scloud


## Analytics

| Cloud Environment | Environment | Display name | App ID | Object Id | SPN Object Id | Subject Name
|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
Public | Dev | dev.analytics.detection.rome.azure.com | fdb4d547-6a66-40f4-bba4-0e30faa293c5 | f23c2a4b-c13b-4b8e-84fb-2e86a75b8344 | 65063f6d-0d43-4ac6-b8cd-d855642a9aeb | dev.analytics.detection.rome.azure.com
Public | Stage | stage.analytics.detection.rome.azure.com | 645c4219-6106-48eb-a2c2-ffd887595315 | bcd7dfaa-81b8-4c85-acb5-aa5a5731e758 | AME: 968b0bca-eb32-4159-aa2f-a7e11d9426df, Corp: b4c91fee-4494-4641-8d16-60a3e45f1ba4 | stage.analytics.detection.rome.azure.com
Public | Prod | prod.analytics.detection.rome.azure.com | be8249e3-9b18-4894-8ec3-67ffe58e951d | e7e92dd7-fa37-4b55-9a50-ad7412acfc7d | AME: 51589449-50c4-4a7a-9c35-8a4f9b2e1c1a CORP: 19024c20-d8bf-43ef-95bd-45ff57905fef | prod.analytics.detection.rome.azure.com
Fairfax | Dev | dev.analytics.detection.rome.azure.us | 6da9932d-569e-4f0c-a841-2048b9839039 | fdef328a-a442-4351-9989-ef006c6db8e2 | 379525d6-bdaf-4f33-ae79-466339d7972e | dev.analytics.detection.rome.azure.us
Fairfax | Stage | stage.analytics.detection.rome.azure.us | 1c2b39e5-54b3-4c9b-838c-77ddf1b28920 | 83665993-83fd-4096-a0f7-4680e44febf7 | 3b46f0f0-06ff-4142-b8b2-c09d6664c5dd | stage.analytics.detection.rome.azure.us
Fairfax | Prod | prod.analytics.detection.rome.azure.us | 45b1e0ef-871d-4c9e-a7ad-afdcda95361b | 03a290cb-c847-4c16-9fa6-fc20944990b7 | acfdfc7b-8116-4141-865a-335439330be3 | prod.analytics.detection.rome.azure.us
Mooncake | Stage | analytics.stage.detection.rome.azure.cn | 9e9a8414-73bd-45e3-886f-5b49cb565ba5 | a0c271a7-2494-49dd-9eee-204a52e2fbbc | 03a44afe-cf6d-4467-9d87-bd69ab7213ce | stage.analytics.detection.rome.azure.cn
Mooncake | Prod | analytics.prod.detection.rome.azure.cn | 96a5c195-4557-4e12-8439-3c9f1bdcb48e | 0f11962e-21d9-4528-bfd6-664568861d12 | e5d4b126-dcc8-4cba-84e4-9136d9d5cbdc | prod.analytics.detection.rome.azure.cn
EX | Prod | prod.analytics.detection.rome.azure.eaglex.ic.gov | 75fb4cae-9b39-4994-b1a6-2e157a9435ed | d66cf21e-bd28-497b-befd-9be577dc2177 | d0a89fdf-7237-4302-b0a3-c1a5e7610791 | prod.analytics.detection.rome.azure.eaglex.ic.gov
RX | Prod | prod.analytics.detection.rome.azure.microsoft.scloud | 9c5d02b1-95d3-4f0f-a096-4a4a4184575a | ba89e9a2-ffad-4768-bc4a-b9563189e8f9 | 0cb49b01-f63d-4aca-9c72-adb8c450391d | prod.analytics.detection.rome.azure.microsoft.scloud


## Discovery

| Cloud Environment | Environment | Display name | App ID | Object Id | SPN Object Id | Subject Name
|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
Public | Dev | dev.discovery.detection.rome.azure.com | 0ed9dc95-f49e-4054-bc52-9836a1b2c257 | c26babc1-41d3-4282-ad9e-8d08cc14cacd | a199c98f-8c14-4550-bfdb-2e16c41915e9 | dev.discovery.detection.rome.azure.com
Public | Stage | stage.discovery.detection.rome.azure.com | 063ebe84-ff38-4b80-bc71-b9d1356f2a0b | 4b68e4c2-619c-4823-8c70-7ab5c3abada6 | AME: a30bcda3-d08a-412d-aea9-fbab4c514eea | stage.discovery.detection.rome.azure.com
Public | Prod | prod.discovery.detection.rome.azure.com | aeed9503-5834-4afe-936b-d52eaba614df | 37475af2-812c-4769-8136-c8c2baa57e12 | AME: 769261f8-cf2b-40e8-89e3-3b72e9f1157e | prod.discovery.detection.rome.azure.com
Fairfax | Dev | dev.discovery.detection.rome.azure.us | 8f6fe1ad-78be-4ea4-9d4b-4418cf64918c | 5e5ed3af-27b1-4acb-b758-784fc2ff6940 | a71fa038-41ae-4104-8d04-c8a2b654b068 | dev.discovery.detection.rome.azure.us
Fairfax | Stage | stage.discovery.detection.rome.azure.us | 19f34dbe-4b76-4184-a4f1-b8e5cfe01bef | e2a08bdd-0611-4b5d-a523-6fae89bc107a | 7cfca54b-24fb-4232-a8fe-8b5d13bbc581 | stage.discovery.detection.rome.azure.us
Fairfax | Prod | prod.discovery.detection.rome.azure.us | 41a2b268-8b3e-42f6-903e-c63bcfe47fb2 | 78f1f8b8-b82f-4e89-8009-72da7f265a08 | 28d13e39-b07a-47c3-b52d-18acf36b9dcf | prod.discovery.detection.rome.azure.us
Mooncake | Stage | discovery.stage.detection.rome.azure.cn | 56ed2eba-8567-4252-b641-21d29c010275 | 7ce278ec-61c2-406f-8b6f-07673c15e69c | 0f185908-d07b-4423-8348-6772bb9b3f3d | stage.discovery.detection.rome.azure.cn
Mooncake | Prod | discovery.prod.detection.rome.azure.cn | 0b903396-322f-4321-a388-f68e9c096335 | 5ed35ac0-c861-4f72-9d07-34aaf08c3f42 | 96575815-7acc-492a-82fc-5f377a6eeed0 | prod.discovery.detection.rome.azure.cn
EX | Prod | prod.discovery.detection.rome.azure.eaglex.ic.gov | 13df9937-7e29-43be-b58b-c5668b226728 | 7c373a14-40e5-434d-a76b-e7df31486bef | 5486bd5c-f3b1-4172-a40d-0f5c47e2a0f2 | prod.discovery.detection.rome.azure.eaglex.ic.gov
RX | Prod | prod.discovery.detection.rome.azure.microsoft.scloud | 51e0b7bf-e247-4d5d-834e-b0ddcc45d6ce | 3819c9d9-98ab-44a9-9e57-1e2a5aae4d3b | a479cbc2-97e1-4b17-a5f4-e6ca9c1297cc | prod.discovery.detection.rome.azure.microsoft.scloud


## Deployment

| Cloud Environment | Environment | Display name | App ID | Object Id | SPN Object Id | Subject Name
|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
Public | Dev | dev.deployment.detection.rome.azure.com | 20487c28-e544-45e7-a130-739156303dbe | bf248b90-f0e9-489b-b974-c99c363dc4d5 | dc0deccc-5c4b-4816-9633-f8d6f2d8485a | dev.deployment.detection.rome.azure.com
Public | Stage | stage.deployment.detection.rome.azure.com | 41a16ff6-f2a8-49e8-be30-30010f1ea7c9 | 927067cb-858a-44e7-83b8-fe89f8ee0291 | 742b3f1e-8be9-46ca-95d8-143dd433206b | stage.deployment.detection.rome.azure.com
Public | Prod | prod.deployment.detection.rome.azure.com | 6d4d88b4-4b80-4299-add9-73c8952a80df | cf2974b9-ae3d-4890-a76d-7781ade34db0 | 74edbb86-c06b-432a-959f-2ed20085b82b | prod.deployment.detection.rome.azure.com
Fairfax | Dev | dev.deployment.detection.rome.azure.us | 60dd3546-ac9b-4443-9abd-0c0412eea693 | 108438ae-9e78-41be-8b08-5f4abc44744e | 21a57b28-7bb2-42a7-a42a-0ab7f017847a | dev.deployment.detection.rome.azure.us
Fairfax | Stage | stage.deployment.detection.rome.azure.us | 19660bc7-f336-493e-9a5a-2ab795ac3f3c | d6db3284-2417-4c79-abc4-e31aa04d69c0 | 310ebbd7-5953-4c6f-a8dc-8acade35295c | stage.deployment.detection.rome.azure.us
Fairfax | Prod | prod.deployment.detection.rome.azure.us | 3c53e8b7-2dab-4517-8ba0-4504f2622d80 | 0f146a18-551d-4ccb-9333-6be56f3c899d | 97362f3b-afa1-44d8-ba11-ad7be251ec2a | prod.deployment.detection.rome.azure.us
Mooncake | Stage | deployment.stage.detection.rome.azure.cn | 96d41487-0413-41b8-8e70-064fa69e6994 | ef0140a5-48d5-42b5-b7a1-1522608536e2 | ab8675a5-32d3-41ac-9ba8-528243f0212a | stage.deployment.detection.rome.azure.cn
Mooncake | Prod | deployment.prod.detection.rome.azure.cn | 6cc92b3e-4389-4d73-9f80-c2825189c5f7 | 04b33681-13b9-4e33-8ac4-0958ed4e9c9c | 00930159-68e9-41fd-a44e-b4b3b641d03d | prod.deployment.detection.rome.azure.cn
EX | Prod | prod.deployment.detection.rome.azure.eaglex.ic.gov | f2b81e7d-9875-42b3-b2cc-49ccffe3e915 | a1b21736-7f39-4a67-ac24-804ccfa0d0b4 | 22e809cd-63a5-4362-851c-2ccd07f53204 | prod.deployment.detection.rome.azure.eaglex.ic.gov
RX | Prod | prod.deployment.detection.rome.azure.microsoft.scloud | 89206caf-7c1d-489e-aec8-f0c6af5efcb8 | b1fbb240-b40a-4681-a7e2-fedaaab39827 | 29e674fc-6613-4880-adf7-d95e12543e33 | prod.deployment.detection.rome.azure.microsoft.scloud