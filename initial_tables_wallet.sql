CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE cashbacks (
   id uuid DEFAULT uuid_generate_v4(),
   sold_at TIMESTAMP NOT NULL,
   customer JSON NOT NULL,
   total DECIMAL NOT NULL,
   products JSONB NOT NULL,
   PRIMARY KEY (id)
);

CREATE TABLE processed_cashbacks (
   id uuid DEFAULT uuid_generate_v4(),
   cashback_id uuid NOT NULL,
   created_at TIMESTAMP NOT NULL,
   message VARCHAR NOT NULL,
   cashback_reference_id INTEGER NOT NULL,
   document VARCHAR NOT NULL,
   cashback DECIMAL NOT NULL,
   PRIMARY KEY (id)
);
