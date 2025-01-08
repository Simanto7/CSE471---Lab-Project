-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 17, 2021 at 04:39 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `djangoshop`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts_customer`
--

CREATE TABLE `accounts_customer` (
  `id` int(11) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `phone` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `date_created` datetime(6) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `profile_pic` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts_customer`
--

INSERT INTO `accounts_customer` (`id`, `name`, `phone`, `email`, `date_created`, `user_id`, `profile_pic`) VALUES
(2, 'A.T.M. Masum Billah', '01719118554', 'masumbillah1717@gmail.com', '2021-02-11 15:36:53.011691', 1, NULL),
(3, 'Masum Billah', '01719118554', 'mishumishu5758@gmail.com', '2021-02-11 22:30:55.298010', 7, NULL),
(6, 'mishu', '01719118554', 'masumbillah1717@gmail.com', '2021-02-17 12:10:33.701850', 10, '');

-- --------------------------------------------------------

--
-- Table structure for table `accounts_order`
--

CREATE TABLE `accounts_order` (
  `id` int(11) NOT NULL,
  `date_created` datetime(6) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `products_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts_order`
--

INSERT INTO `accounts_order` (`id`, `date_created`, `status`, `customer_id`, `products_id`) VALUES
(1, '2021-02-11 22:36:42.877276', '0', 2, 1),
(4, '2021-02-12 23:34:18.611614', '1', 3, 1),
(5, '2021-02-12 23:34:41.731138', '2', 3, 1),
(8, '2021-02-13 06:55:25.647835', '0', 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `accounts_product`
--

CREATE TABLE `accounts_product` (
  `id` int(11) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `price` double DEFAULT NULL,
  `category` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `date_created` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts_product`
--

INSERT INTO `accounts_product` (`id`, `name`, `price`, `category`, `description`, `date_created`) VALUES
(1, 'msi gf 63', 8000, 'Outdoor', 'good gaming laptop', '2021-02-11 22:33:02.313902'),
(2, 'x9', 1000, 'Outdoor', 'good gaming mouse', '2021-02-11 22:34:57.474424');

-- --------------------------------------------------------

--
-- Table structure for table `accounts_product_tags`
--

CREATE TABLE `accounts_product_tags` (
  `id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts_product_tags`
--

INSERT INTO `accounts_product_tags` (`id`, `product_id`, `tag_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 2, 1),
(5, 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `accounts_tag`
--

CREATE TABLE `accounts_tag` (
  `id` int(11) NOT NULL,
  `name` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts_tag`
--

INSERT INTO `accounts_tag` (`id`, `name`) VALUES
(1, 'electronics'),
(2, 'laptop'),
(3, 'mouse'),
(4, 'computer');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'admin'),
(2, 'customer');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add customer', 7, 'add_customer'),
(26, 'Can change customer', 7, 'change_customer'),
(27, 'Can delete customer', 7, 'delete_customer'),
(28, 'Can view customer', 7, 'view_customer'),
(29, 'Can add order', 8, 'add_order'),
(30, 'Can change order', 8, 'change_order'),
(31, 'Can delete order', 8, 'delete_order'),
(32, 'Can view order', 8, 'view_order'),
(33, 'Can add product', 9, 'add_product'),
(34, 'Can change product', 9, 'change_product'),
(35, 'Can delete product', 9, 'delete_product'),
(36, 'Can view product', 9, 'view_product'),
(37, 'Can add tag', 10, 'add_tag'),
(38, 'Can change tag', 10, 'change_tag'),
(39, 'Can delete tag', 10, 'delete_tag'),
(40, 'Can view tag', 10, 'view_tag');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$216000$XA3wJvMq3VBs$AWsCje3C1QC4LJEeEQUcc8I4e6sGWJs/Sdjft4TyemI=', '2021-02-17 12:19:47.612245', 1, 'mishu', '', '', 'mishu@gmail.com', 1, 1, '2021-02-11 15:26:50.000000'),
(7, 'pbkdf2_sha256$216000$qj2Gy6FVVQWA$NZ9RW7QwR0yol9wt3LkwCVtbjqoqM6IahMW0H0dqg+w=', '2021-02-17 14:28:39.260316', 0, 'mb_mishu', '', '', 'mishumishu5758@gmail.com', 0, 1, '2021-02-16 19:35:41.062083'),
(10, 'pbkdf2_sha256$216000$dlCt1oxaIDoM$p9tJlP3vEdaypAERLBtgLqvugp+wzgvA1eQJukx2fiY=', '2021-02-17 12:20:15.000000', 0, 'mbmishu', '', '', 'masumbillah1717@gmail.com', 0, 1, '2021-02-17 12:10:33.000000');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 1, 1),
(7, 7, 2),
(10, 10, 2);

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-02-11 15:35:13.006543', '1', 'Customer object (1)', 1, '[{\"added\": {}}]', 7, 1),
(2, '2021-02-11 15:35:17.214121', '1', 'Customer object (1)', 2, '[]', 7, 1),
(3, '2021-02-11 15:36:46.416890', '1', 'Customer object (1)', 3, '', 7, 1),
(4, '2021-02-11 15:36:53.012964', '2', 'Customer object (2)', 1, '[{\"added\": {}}]', 7, 1),
(5, '2021-02-11 15:39:11.327669', '2', 'A.T.M. Masum Billah', 2, '[]', 7, 1),
(6, '2021-02-11 22:30:55.299009', '3', 'Masum Billah', 1, '[{\"added\": {}}]', 7, 1),
(7, '2021-02-11 22:31:18.057245', '1', 'electronics', 1, '[{\"added\": {}}]', 10, 1),
(8, '2021-02-11 22:31:24.304408', '2', 'laptop', 1, '[{\"added\": {}}]', 10, 1),
(9, '2021-02-11 22:31:31.760336', '3', 'mouse', 1, '[{\"added\": {}}]', 10, 1),
(10, '2021-02-11 22:31:38.969437', '4', 'computer', 1, '[{\"added\": {}}]', 10, 1),
(11, '2021-02-11 22:33:02.318921', '1', 'msi gf 63', 1, '[{\"added\": {}}]', 9, 1),
(12, '2021-02-11 22:33:13.507081', '1', 'msi gf 63', 2, '[]', 9, 1),
(13, '2021-02-11 22:34:57.478366', '2', 'x9', 1, '[{\"added\": {}}]', 9, 1),
(14, '2021-02-11 22:36:42.879250', '1', 'Order object (1)', 1, '[{\"added\": {}}]', 8, 1),
(15, '2021-02-11 22:37:02.084824', '2', 'Order object (2)', 1, '[{\"added\": {}}]', 8, 1),
(16, '2021-02-12 02:32:25.385738', '1', 'Order object (1)', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 8, 1),
(17, '2021-02-12 02:32:30.807442', '2', 'Order object (2)', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 8, 1),
(18, '2021-02-12 02:32:44.854090', '1', 'Order object (1)', 2, '[]', 8, 1),
(19, '2021-02-12 02:32:49.236561', '2', 'Order object (2)', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 8, 1),
(20, '2021-02-12 03:26:34.751387', '2', 'x9', 2, '[{\"changed\": {\"fields\": [\"tags\"]}}]', 9, 1),
(21, '2021-02-12 13:25:59.900951', '2', 'Order object (2)', 2, '[{\"changed\": {\"fields\": [\"products\"]}}]', 8, 1),
(22, '2021-02-12 13:26:13.076530', '2', 'Order object (2)', 3, '', 8, 1),
(23, '2021-02-12 13:26:20.834192', '3', 'Order object (3)', 1, '[{\"added\": {}}]', 8, 1),
(24, '2021-02-15 23:42:39.733123', '2', 'mishu1', 3, '', 4, 1),
(25, '2021-02-16 15:05:17.045735', '3', 'mbmishu', 3, '', 4, 1),
(26, '2021-02-16 15:06:40.042355', '4', 'mbmishu', 3, '', 4, 1),
(27, '2021-02-16 15:08:26.489359', '5', 'mbmishu', 3, '', 4, 1),
(28, '2021-02-16 17:40:01.073478', '1', 'admin', 1, '[{\"added\": {}}]', 3, 1),
(29, '2021-02-16 17:40:07.360046', '2', 'customer', 1, '[{\"added\": {}}]', 3, 1),
(30, '2021-02-16 17:40:15.811761', '1', 'mishu', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(31, '2021-02-16 17:40:21.910511', '6', 'mbmishu', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(32, '2021-02-16 18:16:56.548084', '6', 'mbmishu', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(33, '2021-02-16 18:29:35.411715', '6', 'mbmishu', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(34, '2021-02-16 19:02:09.013952', '6', 'mbmishu', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(35, '2021-02-16 19:06:05.508064', '6', 'mbmishu', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(36, '2021-02-16 19:06:24.370154', '6', 'mbmishu', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(37, '2021-02-16 19:20:12.139872', '6', 'mbmishu', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(38, '2021-02-16 19:24:55.927763', '6', 'mbmishu', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(39, '2021-02-16 19:29:39.730550', '6', 'mbmishu', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(40, '2021-02-16 22:31:40.056334', '2', 'A.T.M. Masum Billah', 2, '[{\"changed\": {\"fields\": [\"User\"]}}]', 7, 1),
(41, '2021-02-16 22:31:45.530159', '3', 'Masum Billah', 2, '[{\"changed\": {\"fields\": [\"User\"]}}]', 7, 1),
(42, '2021-02-16 23:06:40.547540', '6', 'mbmishu', 3, '', 4, 1),
(43, '2021-02-17 10:31:11.515845', '4', 'mishui', 3, '', 7, 1),
(44, '2021-02-17 10:32:00.259956', '8', 'mbmishu', 3, '', 4, 1),
(45, '2021-02-17 11:04:41.502101', '5', 'A.T.M. Masum Billah', 2, '[{\"changed\": {\"fields\": [\"Name\", \"Phone\", \"Email\", \"Profile pic\"]}}]', 7, 1),
(46, '2021-02-17 11:42:10.258119', '5', 'mishu22', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 7, 1),
(47, '2021-02-17 11:48:25.202451', '5', 'mishu22', 2, '[{\"changed\": {\"fields\": [\"Email\"]}}]', 7, 1),
(48, '2021-02-17 12:09:52.077568', '5', 'mishu420', 3, '', 7, 1),
(49, '2021-02-17 12:10:24.818205', '9', 'mbmishu', 3, '', 4, 1),
(50, '2021-02-17 12:18:01.429530', '6', 'mishu', 2, '[{\"changed\": {\"fields\": [\"Profile pic\"]}}]', 7, 1),
(51, '2021-02-17 12:18:11.371378', '6', 'mishu', 2, '[{\"changed\": {\"fields\": [\"Profile pic\"]}}]', 7, 1),
(52, '2021-02-17 12:18:19.713548', '6', 'mishu', 2, '[{\"changed\": {\"fields\": [\"Profile pic\"]}}]', 7, 1),
(53, '2021-02-17 14:27:27.708006', '10', 'mbmishu', 2, '[{\"changed\": {\"fields\": [\"Email address\"]}}]', 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'accounts', 'customer'),
(8, 'accounts', 'order'),
(9, 'accounts', 'product'),
(10, 'accounts', 'tag'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-02-11 15:12:30.713876'),
(2, 'auth', '0001_initial', '2021-02-11 15:12:31.574334'),
(3, 'admin', '0001_initial', '2021-02-11 15:12:31.911388'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-02-11 15:12:31.923355'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-02-11 15:12:31.948529'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-02-11 15:12:32.073936'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-02-11 15:12:32.148661'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-02-11 15:12:32.173300'),
(9, 'auth', '0004_alter_user_username_opts', '2021-02-11 15:12:32.185034'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-02-11 15:12:32.255521'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-02-11 15:12:32.258512'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-02-11 15:12:32.270483'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-02-11 15:12:32.295345'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-02-11 15:12:32.316293'),
(15, 'sessions', '0001_initial', '2021-02-11 15:12:32.386103'),
(16, 'accounts', '0001_initial', '2021-02-11 15:32:42.049682'),
(17, 'accounts', '0002_order_product', '2021-02-11 15:47:36.593578'),
(18, 'accounts', '0003_auto_20210212_0418', '2021-02-11 22:18:52.209966'),
(19, 'accounts', '0004_auto_20210212_0423', '2021-02-11 22:23:35.704810'),
(20, 'accounts', '0005_auto_20210212_0425', '2021-02-11 22:25:44.274775'),
(21, 'accounts', '0006_auto_20210212_0429', '2021-02-11 22:29:29.746804'),
(22, 'accounts', '0007_auto_20210212_0434', '2021-02-11 22:34:13.454467'),
(23, 'accounts', '0008_auto_20210212_0830', '2021-02-12 02:30:33.062841'),
(24, 'accounts', '0009_auto_20210212_0831', '2021-02-12 02:31:56.303308'),
(25, 'auth', '0010_alter_group_name_max_length', '2021-02-16 22:28:44.736045'),
(26, 'auth', '0011_update_proxy_permissions', '2021-02-16 22:28:44.740033'),
(27, 'auth', '0012_alter_user_first_name_max_length', '2021-02-16 22:28:44.767675'),
(28, 'accounts', '0010_customer_user', '2021-02-16 22:31:09.893278'),
(29, 'accounts', '0011_customer_profile_pic', '2021-02-17 11:01:08.585889'),
(30, 'accounts', '0012_auto_20210217_1808', '2021-02-17 12:08:55.480156');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('5riftf1u9u6lh4yk78oj87bf9llu0ts2', '.eJxVjDkOwjAUBe_iGlm2YrxQ0nMG6_svOIBsKUuFuDuJlALamXnvrTKsS83rzFMeSV2UVadfVgCf3HZBD2j3rrG3ZRqL3hN92FnfOvHrerR_BxXmuq1NDBJJigXnOFAiI4JmQw5NCuwluRgHgwE4IYeIdB5EEjjjrfVlUJ8vBOE4gg:1lC4sr:5oPr_VsoV9i5ZGJFsqfninwFecDyde2J_fpFIBLlHrw', '2021-03-02 18:15:37.965954'),
('7us5s6v40f5w3uh9pagnvhmdu1slxyho', '.eJxVjDkOwjAUBe_iGlm2YrxQ0nMG6_svOIBsKUuFuDuJlALamXnvrTKsS83rzFMeSV2UVadfVgCf3HZBD2j3rrG3ZRqL3hN92FnfOvHrerR_BxXmuq1NDBJJigXnOFAiI4JmQw5NCuwluRgHgwE4IYeIdB5EEjjjrfVlUJ8vBOE4gg:1lCLDR:XeBIvs5QJhyZ3WGMACPk4m3FY137u3w9O7DHobRMAq0', '2021-03-03 11:41:57.750571'),
('a9idsfkbn1wmizmrvwoex9ra7hvj8lmj', '.eJxVjDkOwjAUBe_iGlm2YrxQ0nMG6_svOIBsKUuFuDuJlALamXnvrTKsS83rzFMeSV2UVadfVgCf3HZBD2j3rrG3ZRqL3hN92FnfOvHrerR_BxXmuq1NDBJJigXnOFAiI4JmQw5NCuwluRgHgwE4IYeIdB5EEjjjrfVlUJ8vBOE4gg:1lCK3s:nx1Q02FXomHbheSqeEnERjeLUG-MMCpfjpHSEkk1a0E', '2021-03-03 10:28:00.918676'),
('h8194e4fj9gbke2a3kpzqsdag654ada0', '.eJxVjDsOwjAQBe_iGln-gD-U9JzBWu-ucQDZUpxUiLtDpBTQvpl5L5FgXWpaB89pInEWXhx-twz44LYBukO7dYm9LfOU5abInQ557cTPy-7-HVQY9VuDZbJw1EhcwAeLQCeHxrAGFYv3rJVDRaiLdZBBe0UBXIxK-2hccOL9ARB9OCo:1lCNol:3Ntx5CeD9v3QE_grLbM1aXcTvNwuTMx80cKgru72iIg', '2021-03-03 14:28:39.263308');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts_customer`
--
ALTER TABLE `accounts_customer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `accounts_order`
--
ALTER TABLE `accounts_order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `accounts_order_customer_id_23c59287_fk_accounts_customer_id` (`customer_id`),
  ADD KEY `accounts_order_products_id_15dff62d_fk_accounts_product_id` (`products_id`);

--
-- Indexes for table `accounts_product`
--
ALTER TABLE `accounts_product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `accounts_product_tags`
--
ALTER TABLE `accounts_product_tags`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `accounts_product_tags_product_id_tag_id_f558f1ef_uniq` (`product_id`,`tag_id`),
  ADD KEY `accounts_product_tags_tag_id_f4ba4ec3_fk_accounts_tag_id` (`tag_id`);

--
-- Indexes for table `accounts_tag`
--
ALTER TABLE `accounts_tag`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts_customer`
--
ALTER TABLE `accounts_customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `accounts_order`
--
ALTER TABLE `accounts_order`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `accounts_product`
--
ALTER TABLE `accounts_product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `accounts_product_tags`
--
ALTER TABLE `accounts_product_tags`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `accounts_tag`
--
ALTER TABLE `accounts_tag`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounts_customer`
--
ALTER TABLE `accounts_customer`
  ADD CONSTRAINT `accounts_customer_user_id_11606857_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `accounts_order`
--
ALTER TABLE `accounts_order`
  ADD CONSTRAINT `accounts_order_customer_id_23c59287_fk_accounts_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `accounts_customer` (`id`),
  ADD CONSTRAINT `accounts_order_products_id_15dff62d_fk_accounts_product_id` FOREIGN KEY (`products_id`) REFERENCES `accounts_product` (`id`);

--
-- Constraints for table `accounts_product_tags`
--
ALTER TABLE `accounts_product_tags`
  ADD CONSTRAINT `accounts_product_tags_product_id_2d1c4b64_fk_accounts_product_id` FOREIGN KEY (`product_id`) REFERENCES `accounts_product` (`id`),
  ADD CONSTRAINT `accounts_product_tags_tag_id_f4ba4ec3_fk_accounts_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `accounts_tag` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
