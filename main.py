from loguru import logger

logger.add("logs.log", rotation="100 KB", compression="zip", retention=3)

new_level = logger.level("SNAKY", no=38, color="<yellow>", icon="🐍")


@logger.catch
def foo():
    raise ValueError('value incorrect')


@logger.catch(message='Don\'t divide be zero!!!')
def buzz(x: int) -> float:
    return 1 / x


def main() -> int:
    logger.debug('DEBUG 1')
    logger.info('INGO 1')
    logger.warning('WARNING 1')
    logger.error('ERROR 1')
    logger.log("SNAKY", "Here we go!")

    for i in range(100):
        logger.info(f'{i=}')

    try:
        buzz(0)
    except ValueError:
        pass

    try:
        foo()
    except ValueError:
        return 1

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
