# Big Query:


## Infrastructure

- columnar
- capacitor (file format)
- colossus (distributed file system)
- storage optimization
    - partitioning
    - clustering

```sql
CREATE TABLE `project-id.my_dataset.order_items` (
    order_id int64,
    ...
)
PARTITION BY date(created_at)
CLUSTER BY customer_id
```
- dremel (query engine, cluster compute, slots)
