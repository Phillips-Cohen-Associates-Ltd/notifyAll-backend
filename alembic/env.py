from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from os.path import dirname, abspath
import sys
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from os.path import dirname, abspath
import sys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from app.config.config import settings
from app.models import decedent_request_document_draft_model, usermodel, creditor_property_utility_details_model, creditor_property_utility_model, creditor_property_utility_draft_model, creditor_service_utility_draft_model, creditor_service_utility_model,creditor_transfer_details_model,decedent_companies_model,decedent_letter_of_direction_draft_model,decedent_membership_account_draft_model,decedent_membership_accounts_model, decedent_new_creditors_draft_models,decedent_new_creditors_models, decedent_request_creditors_draft_model,decedent_request_creditors_models,decedent_requests_model, decedent_request_document_model,decedent_requests_draft_model, creditor_property_utility_details_draft_model,countries_state_citymodel
from app.config.database import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# here we allow ourselves to pass interpolation vars to alembic.ini
# fron the env
section = config.config_ini_section
config.set_section_option(section, "DB_USER", settings.POSTGRES_USER)
config.set_section_option(section, "DB_PASS", settings.POSTGRES_PASSWORD)
config.set_section_option(section, "DB_HOST", settings.POSTGRES_HOSTNAME)
config.set_section_option(section, "DB_NAME", settings.POSTGRES_DB)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy."
        # poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()