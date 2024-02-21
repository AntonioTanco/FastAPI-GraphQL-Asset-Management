# 🔥FastAPI+📈GraphQL Asset Management Backend

<h2>Project Overview</h2>
<p>Used FastAPI + GraphQL + MongoDB to create a backend for an Asset Management System which allows us to create, read, update and delete Assets using GraphQL queries and mutations. This simplifies the asset management process for IT Professionals by allowing us to query for assets with the exact data we need rather than receiving a huge data payload which would reduce performanace over time in comparison to a Traditional Rest API implementation.</p>

<p>It was a conscious design decision to use GraphQL for a system like this since most IT Professionals and Organizations struggle with Asset Management at scale. The advantage of this implementation is that it is highly extensible allowing for Organizations to log, track and audit Assets which may be spread across a combination of different RRM and MDM solutions that don't exactly offer support for asset tracking/management cross-platform natively. You can tie all of your assets under one simple endpoint which makes auditing at scale even easier.</p>

<h2>Project Features</h2>

- <strong>Only returns the data you want to fetch about an Asset thanks to GraphQL</strong>
- <strong>Database Caching using Redis, using the <i>Cache-aside</i> pattern</strong>
- <strong>CLI Tool which returns all of the Assets in the database</strong>
- <strong>.YML Config which can be customized per use case</strong>
- <strong>Logs which are generated whenever an Asset is created or deleted from a mutation</strong>
- <strong>Containerized Entire Application using <i>Docker</i> for quick and easy deployments<strong>
- <strong>Exensible solution for any organization of any size, can support schema coden using Pydantic</strong>

<h4>Language/Software Used</h4>
- 🐍 Python V3.11.5

___
<h2>System Design</h2>
![Asset Management - System Design](https://github.com/AntonioTanco/FastAPI-GraphQL-Asset-Management/assets/43735570/11ac9794-b394-42c8-bb8a-9da8acc91b2b)
