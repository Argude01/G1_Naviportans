-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-05-2021 a las 16:59:32
-- Versión del servidor: 10.4.18-MariaDB
-- Versión de PHP: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_restaurante`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_direcciones`
--

CREATE TABLE `tbl_direcciones` (
  `ID_DIRECCION` int(11) NOT NULL,
  `DIRECCION` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tbl_direcciones`
--

INSERT INTO `tbl_direcciones` (`ID_DIRECCION`, `DIRECCION`) VALUES
(1, 'Bo. Santa Lucía'),
(2, 'Barrio Toróndon'),
(3, 'Barrio Abajo'),
(4, 'Colonia Casa Blanca'),
(5, 'Barrio Arriba');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_envios`
--

CREATE TABLE `tbl_envios` (
  `ID_ENVIO` int(11) NOT NULL,
  `DESCRIPCION_ENVIO` varchar(300) NOT NULL,
  `FECHA` date NOT NULL,
  `DIRECCION` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tbl_envios`
--

INSERT INTO `tbl_envios` (`ID_ENVIO`, `DESCRIPCION_ENVIO`, `FECHA`, `DIRECCION`) VALUES
(1, 'Almuerzo', '2021-05-21', 'Barrio Arriba'),
(2, 'refresco', '2021-05-21', 'Barrio Arriba');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_facturas`
--

CREATE TABLE `tbl_facturas` (
  `ID_FACTURA` int(11) NOT NULL,
  `DESCRIPCION_FACTURA` varchar(200) NOT NULL,
  `FECHA` date NOT NULL,
  `ID_DIRECCION` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_inventario`
--

CREATE TABLE `tbl_inventario` (
  `ID_PRODUCTO` int(11) NOT NULL,
  `PRODUCTO` varchar(100) DEFAULT NULL,
  `PRECIO` double NOT NULL,
  `ID_DIRECCION` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tbl_inventario`
--

INSERT INTO `tbl_inventario` (`ID_PRODUCTO`, `PRODUCTO`, `PRECIO`, `ID_DIRECCION`) VALUES
(1, 'shampoo', 200, 4),
(2, 'Jabón', 50, 4),
(4, '', 0, 1),
(5, 'PASTA DE DIENTES', 0, 2),
(6, NULL, 0, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_pedidos`
--

CREATE TABLE `tbl_pedidos` (
  `ID_PEDIDO` int(11) NOT NULL,
  `DESCRIPCION_PEDIDO` varchar(200) NOT NULL,
  `FECHA` date NOT NULL,
  `ID_DIRECCION` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tbl_direcciones`
--
ALTER TABLE `tbl_direcciones`
  ADD PRIMARY KEY (`ID_DIRECCION`);

--
-- Indices de la tabla `tbl_envios`
--
ALTER TABLE `tbl_envios`
  ADD PRIMARY KEY (`ID_ENVIO`);

--
-- Indices de la tabla `tbl_facturas`
--
ALTER TABLE `tbl_facturas`
  ADD PRIMARY KEY (`ID_FACTURA`),
  ADD KEY `FK_DIRECCIONES_FACTURAS` (`ID_DIRECCION`);

--
-- Indices de la tabla `tbl_inventario`
--
ALTER TABLE `tbl_inventario`
  ADD PRIMARY KEY (`ID_PRODUCTO`),
  ADD KEY `FK_DIRECCIONES_INVENTARIO` (`ID_DIRECCION`);

--
-- Indices de la tabla `tbl_pedidos`
--
ALTER TABLE `tbl_pedidos`
  ADD PRIMARY KEY (`ID_PEDIDO`),
  ADD KEY `FK_DIRECCIONES_PEDIDOS` (`ID_DIRECCION`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tbl_direcciones`
--
ALTER TABLE `tbl_direcciones`
  MODIFY `ID_DIRECCION` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `tbl_envios`
--
ALTER TABLE `tbl_envios`
  MODIFY `ID_ENVIO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tbl_facturas`
--
ALTER TABLE `tbl_facturas`
  MODIFY `ID_FACTURA` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tbl_inventario`
--
ALTER TABLE `tbl_inventario`
  MODIFY `ID_PRODUCTO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `tbl_pedidos`
--
ALTER TABLE `tbl_pedidos`
  MODIFY `ID_PEDIDO` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tbl_facturas`
--
ALTER TABLE `tbl_facturas`
  ADD CONSTRAINT `FK_DIRECCIONES_FACTURAS` FOREIGN KEY (`ID_DIRECCION`) REFERENCES `tbl_direcciones` (`ID_DIRECCION`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `tbl_inventario`
--
ALTER TABLE `tbl_inventario`
  ADD CONSTRAINT `FK_DIRECCIONES_INVENTARIO` FOREIGN KEY (`ID_DIRECCION`) REFERENCES `tbl_direcciones` (`ID_DIRECCION`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `tbl_pedidos`
--
ALTER TABLE `tbl_pedidos`
  ADD CONSTRAINT `FK_DIRECCIONES_PEDIDOS` FOREIGN KEY (`ID_DIRECCION`) REFERENCES `tbl_direcciones` (`ID_DIRECCION`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
