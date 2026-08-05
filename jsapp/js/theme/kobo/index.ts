import { createTheme, rem } from '@mantine/core'
import { ActionIconThemeKobo } from './ActionIcon'
import { AlertThemeKobo } from './Alert'
import { AutocompleteThemeKobo } from './Autocomplete'
import { ButtonThemeKobo } from './Button'
import { CheckboxThemeKobo } from './Checkbox'
import { DividerThemeKobo } from './Divider'
import { InputBaseThemeKobo } from './InputBase'
import { LoaderThemeKobo } from './Loader'
import { MenuThemeKobo } from './Menu'
import { ModalThemeKobo } from './Modal'
import { MultiSelectThemeKobo } from './MultiSelect'
import { NotificationThemeKobo } from './Notification'
import { NumberInputThemeKobo } from './NumberInput'
import { PaperThemeKobo } from './Paper'
import { PillThemeKobo } from './Pill'
import { RadioThemeKobo } from './Radio'
import { SelectThemeKobo } from './Select'
import { TableThemeKobo } from './Table'
import { TagsInputThemeKobo } from './TagsInput'
import { ThemeIconThemeKobo } from './ThemeIcon'
import { TooltipThemeKobo } from './Tooltip'

export const themeKobo = createTheme({
  primaryColor: 'blue',
  colors: {
    gray: [
      '#1A1A1A',
      '#2E2C2B',
      '#5D5855',
      '#817A76',
      '#A39B97',
      '#C3BCB8',
      '#DDD8D5',
      '#EEEAE8',
      '#F8F6F5',
      'hsl(0, 0%, 100%)', // [9] #ffffff, white background
    ],
    blue: ['#000', '#000', '#000', '#000', '#9F331C', '#B83D24', '#C94327', '#FFAB98', '#FFD8CF', '#FFF2EE'],
    teal: [
      '#000',
      '#000',
      'hsl(185, 57%, 25%)', // #1b5e64
      'hsl(185, 57%, 35%)', // #26838c
      'hsl(185, 57%, 57%)', // #52c5d0
      'hsl(186, 57%, 75%)', // #9bdde4
      'hsl(185, 58%, 85%)', // #c3ebef
      'hsl(188, 60%, 95%)', // #ebf8fa
      '#000',
      '#000',
    ],
    red: [
      '#000',
      '#000',
      '#000',
      '#000',
      '#000',
      'hsl(0, 100%, 26%)', // #850000
      'hsl(0, 100%, 31%)', // #9d0000
      'hsl(0, 100%, 75%)', // #ff8080
      'hsl(0, 100%, 90%)', // #ffcccc
      'hsl(0, 100%, 96%)', // #ffe9e9
    ],
    amber: [
      '#000',
      '#000',
      '#000',
      '#000',
      '#000',
      'hsl(30, 100%, 25%)', // #803f00 ($kobo-dark-amber)
      'hsl(29, 100%, 75%)', // #ffbe80 ($kobo-amber)
      'hsl(30, 100%, 90%)', // #ffe8cc ($kobo-light-amber)
      '#000',
      '#000',
    ],
  },

  other: {
    datamovinPrimary: '#FF6D4D',
    datamovinPrimaryDark: '#E05030',
    datamovinInk: '#1A1A1A',
    datamovinSurface: '#F8F6F5',
  },

  // Typography
  scale: 16 / 14, // Because old ways set base font to 14px instead of standard 16px.
  fontFamily: '"Inter", "Roboto", sans-serif',
  fontFamilyMonospace: 'Roboto Mono, monospace',
  fontSizes: {
    xs: rem(12),
    sm: rem(13), // TODO: For now implied from button sizes.
    md: rem(14), // TODO: For now implied from button sizes.
    lg: rem(16),
    xl: rem(18),
  },
  // Kobo uses 20+ different line-heights in different units. TODO: standardize and use mantine config.
  lineHeights: {},
  headings: {
    fontWeight: '500',
  },
  // headings: {
  //   fontFamily: '"Roboto", sans-serif',
  // },

  defaultRadius: 'md',
  radius: {
    xs: '2px',
    sm: '4px',
    md: '6px',
    lg: '10px',
    xl: '14px',
  },

  spacing: {
    xxs: '8px',
  },

  components: {
    ActionIcon: ActionIconThemeKobo,
    Alert: AlertThemeKobo,
    Button: ButtonThemeKobo,
    InputBase: InputBaseThemeKobo,
    Loader: LoaderThemeKobo,
    Menu: MenuThemeKobo,
    Modal: ModalThemeKobo,
    MultiSelect: MultiSelectThemeKobo,
    Select: SelectThemeKobo,
    Tooltip: TooltipThemeKobo,
    Table: TableThemeKobo,
    Divider: DividerThemeKobo,
    TagsInput: TagsInputThemeKobo,
    ThemeIcon: ThemeIconThemeKobo,
    NumberInput: NumberInputThemeKobo,
    Paper: PaperThemeKobo,
    Pill: PillThemeKobo,
    Checkbox: CheckboxThemeKobo,
    Radio: RadioThemeKobo,
    Notification: NotificationThemeKobo,
    Autocomplete: AutocompleteThemeKobo,
  },
})
