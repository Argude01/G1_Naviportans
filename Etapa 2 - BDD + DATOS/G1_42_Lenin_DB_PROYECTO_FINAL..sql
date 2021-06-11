-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-06-2021 a las 01:34:27
-- Versión del servidor: 10.4.18-MariaDB
-- Versión de PHP: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_naviportans`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_categoria`
--

CREATE TABLE `tbl_categoria` (
  `ID_CATEGORIA` int(11) NOT NULL,
  `CATEGORIA` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tbl_categoria`
--

INSERT INTO `tbl_categoria` (`ID_CATEGORIA`, `CATEGORIA`) VALUES
(1, 'COMIDA'),
(2, 'BEBIDAS'),
(3, 'REFRIGERADOS');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_pedidos`
--

CREATE TABLE `tbl_pedidos` (
  `ID_PEDIDOS` int(11) NOT NULL,
  `FECHA` date DEFAULT NULL,
  `ID_PRODUCTO` int(11) DEFAULT NULL,
  `ID_USUARIO` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tbl_pedidos`
--

INSERT INTO `tbl_pedidos` (`ID_PEDIDOS`, `FECHA`, `ID_PRODUCTO`, `ID_USUARIO`) VALUES
(1, '2021-06-16', 4, 2),
(2, '2021-06-17', 3, 5),
(3, '2021-06-29', 2, 2),
(4, '2021-07-20', 1, 3),
(5, '2021-06-20', 5, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_productos`
--

CREATE TABLE `tbl_productos` (
  `ID_PRODUCTO` int(11) NOT NULL,
  `NOMBRE` varchar(200) DEFAULT NULL,
  `EXISTENCIAS` int(11) DEFAULT NULL,
  `DESCRIPCION` varchar(300) DEFAULT NULL,
  `PRECIO` int(11) DEFAULT NULL,
  `FECHA_VENCIMIENTO` date NOT NULL,
  `ID_CATEGORIA` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tbl_productos`
--

INSERT INTO `tbl_productos` (`ID_PRODUCTO`, `NOMBRE`, `EXISTENCIAS`, `DESCRIPCION`, `PRECIO`, `FECHA_VENCIMIENTO`, `ID_CATEGORIA`) VALUES
(1, 'Manzanas', 120, 'Manzanas Rojas', 250, '2021-06-11', 1),
(2, 'Bebida de Naranja\r\n', 140, 'Bebida Natural de Naranja Embotellada\r\n', 40, '2021-07-22', 2),
(3, 'Bebida de Naranja\r\n', 140, 'Bebida Natural de Naranja Embotellada\r\n', 40, '2021-08-05', 3),
(4, 'Fresas\r\n', 421, 'Fresas Frescas\r\n', 12, '2021-09-09', 1),
(5, 'Helado Chocolate\r\n', 1141, 'Helado de sabor Chocolate\r\n', 52, '2021-08-10', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_usuarios`
--

CREATE TABLE `tbl_usuarios` (
  `ID_USUARIO` int(11) NOT NULL,
  `NOMBRE` varchar(200) DEFAULT NULL,
  `CORREO` varchar(200) DEFAULT NULL,
  `CONTRASEÑA` varchar(100) DEFAULT NULL,
  `DIRECCION` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tbl_usuarios`
--

INSERT INTO `tbl_usuarios` (`ID_USUARIO`, `NOMBRE`, `CORREO`, `CONTRASEÑA`, `DIRECCION`) VALUES
(1, 'FERNANDO DISCUA', 'fertsub@gmail.com', 'estanoesmicontraseña123', 'Barrio Suyapa 2 cuadras arriba del Kinder Carlos Miranda`DIRRECION`'),
(2, 'FERNANDO MACHADO', 'FEERNDA_MACH12@gmail.com', 'password456', 'Barrio Arriba'),
(3, 'JUAN FLORES', 'flores12@outlook.es\r\n', '8798dh56s4f6\r\n', 'Colonia Lomas del Rio\r\n'),
(4, 'Jostin Castillo\r\n', 'javierf89@yahoo.es\r\n', 'jk346bkj346lk\r\n', 'Colonia La Boquin\r\n'),
(5, 'Daniel Bustillo\r\n', 'daniel2452@hotmail.com\r\n', '526642aggajl\r\n', 'Colonia 1º de Mayo\r\n');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tbl_categoria`
--
ALTER TABLE `tbl_categoria`
  ADD PRIMARY KEY (`ID_CATEGORIA`);

--
-- Indices de la tabla `tbl_pedidos`
--
ALTER TABLE `tbl_pedidos`
  ADD PRIMARY KEY (`ID_PEDIDOS`),
  ADD KEY `FK_PRODUCTO_PEDIDOS` (`ID_PRODUCTO`),
  ADD KEY `FK_USUARIO_PEDIDOS` (`ID_USUARIO`);

--
-- Indices de la tabla `tbl_productos`
--
ALTER TABLE `tbl_productos`
  ADD PRIMARY KEY (`ID_PRODUCTO`),
  ADD KEY `FK_PRODUCTOS_CATEGORIAS` (`ID_CATEGORIA`);

--
-- Indices de la tabla `tbl_usuarios`
--
ALTER TABLE `tbl_usuarios`
  ADD PRIMARY KEY (`ID_USUARIO`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tbl_categoria`
--
ALTER TABLE `tbl_categoria`
  MODIFY `ID_CATEGORIA` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `tbl_pedidos`
--
ALTER TABLE `tbl_pedidos`
  MODIFY `ID_PEDIDOS` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `tbl_productos`
--
ALTER TABLE `tbl_productos`
  MODIFY `ID_PRODUCTO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `tbl_usuarios`
--
ALTER TABLE `tbl_usuarios`
  MODIFY `ID_USUARIO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tbl_pedidos`
--
ALTER TABLE `tbl_pedidos`
  ADD CONSTRAINT `FK_PRODUCTO_PEDIDOS` FOREIGN KEY (`ID_PRODUCTO`) REFERENCES `tbl_productos` (`ID_PRODUCTO`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_USUARIO_PEDIDOS` FOREIGN KEY (`ID_USUARIO`) REFERENCES `tbl_usuarios` (`ID_USUARIO`);

--
-- Filtros para la tabla `tbl_productos`
--
ALTER TABLE `tbl_productos`
  ADD CONSTRAINT `FK_PRODUCTOS_CATEGORIAS` FOREIGN KEY (`ID_CATEGORIA`) REFERENCES `tbl_categoria` (`ID_CATEGORIA`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
