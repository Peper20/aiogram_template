from fluent.runtime import FluentLocalization, FluentResourceLoader


loader = FluentResourceLoader('l10n/{locale}')
l10n = FluentLocalization(['ru'], ['main.ftl'], loader)

