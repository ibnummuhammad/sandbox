MERGE INTO iceberg.datalake_iceberg.coin_matching_engine__orders_partitioned_backup_test_5 t
USING (SELECT * FROM iceberg.datalake_iceberg.coin_matching_engine__orders_partitioned_backup WHERE processed_date >= DATE '2025-03-17' AND processed_date <= DATE '2025-04-23') s
ON t.processed_date = s.processed_date and t.id = s.id
WHEN MATCHED THEN
    UPDATE SET 
        amount = s.amount,
        avg_traded_price = s.avg_traded_price,
        client_id = s.client_id,
        client_order_id = s.client_order_id,
        client_user_id = s.client_user_id,
        created_at = s.created_at,
        created_by = s.created_by,
        deleted_at = s.deleted_at,
        executed_amount = s.executed_amount,
        partition_date = s.partition_date,
        payment_status = s.payment_status,
        price = s.price,
        quantity = s.quantity,
        quantity_filled = s.quantity_filled,
        reason = s.reason,
        self_trading = s.self_trading,
        side = s.side,
        status = s.status,
        stp_mode = s.stp_mode,
        symbol = s.symbol,
        synced_at = s.synced_at,
        type = s.type,
        updated_at = s.updated_at,
        processed_date = s.processed_date,
        processed_timestamp = s.processed_timestamp
WHEN NOT MATCHED THEN
    INSERT (id, amount, avg_traded_price, client_id, client_order_id, client_user_id, created_at, created_by, deleted_at, executed_amount, partition_date, payment_status, price, quantity, quantity_filled, reason, self_trading, side, status, stp_mode, symbol, synced_at, type, updated_at, processed_date, processed_timestamp)
    VALUES (s.id, s.amount, s.avg_traded_price, s.client_id, s.client_order_id, s.client_user_id, s.created_at, s.created_by, s.deleted_at, s.executed_amount, s.partition_date, s.payment_status, s.price, s.quantity, s.quantity_filled, s.reason, s.self_trading, s.side, s.status, s.stp_mode, s.symbol, s.synced_at, s.type, s.updated_at, s.processed_date, s.processed_timestamp);