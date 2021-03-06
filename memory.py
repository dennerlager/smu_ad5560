class Memory:
    def __init__(self):
        self.registers = {'nop': 0x00,
                          'system_control': 0x01,
                          'dps_1': 0x02,
                          'dps_2': 0x03,
                          'compensation_1': 0x04,
                          'compensation_2': 0x05,
                          'alarm_setup': 0x06,
                          'diagnostic': 0x07,
                          'fin_dac_x1': 0x08,
                          'fin_dac_m': 0x09,
                          'fin_dac_c': 0x0a,
                          'offset_dac_x': 0x0b,
                          'osd_dac_x': 0x0c,
                          'cll_dac_x1': 0x0d,
                          'cll_dac_m': 0x0e,
                          'cll_dac_c': 0x0f,

                          'clh_dac_x1': 0x10,
                          'clh_dac_m': 0x11,
                          'clh_dac_c': 0x12,
                          'cpl_dac_x1_5uA': 0x13,
                          'cpl_dac_m_5uA': 0x14,
                          'cpl_dac_c_5uA': 0x15,
                          'cpl_dac_x1_25uA': 0x16,
                          'cpl_dac_m_25uA': 0x17,
                          'cpl_dac_c_25uA': 0x18,
                          'cpl_dac_x1_250uA': 0x19,
                          'cpl_dac_m_250uA': 0x1a,
                          'cpl_dac_c_250uA': 0x1b,
                          'cpl_dac_x1_2.5mA': 0x1c,
                          'cpl_dac_m_2.5mA': 0x1d,
                          'cpl_dac_c_2.5mA': 0x1e,
                          'cpl_dac_x1_25mA': 0x1f,

                          'cpl_dac_m_25mA': 0x20,
                          'cpl_dac_c_25mA': 0x21,
                          'cpl_dac_x1_ext_range_2': 0x22,
                          'cpl_dac_m_ext_range_2': 0x23,
                          'cpl_dac_c_ext_range_2': 0x24,
                          'cpl_dac_x1_ext_range_1': 0x25,
                          'cpl_dac_m_ext_range_1': 0x26,
                          'cpl_dac_c_ext_range_1': 0x27,
                          'cph_dac_x1_5uA': 0x28,
                          'cph_dac_m_5uA': 0x29,
                          'cph_dac_c_5uA': 0x2a,
                          'cph_dac_x1_25uA': 0x2b,
                          'cph_dac_m_25uA': 0x2c,
                          'cph_dac_c_25uA': 0x2d,
                          'cph_dac_x1_250uA': 0x2e,
                          'cph_dac_m_250uA': 0x2f,

                          'cph_dac_c_250uA': 0x30,
                          'cph_dac_x1_2.5mA': 0x31,
                          'cph_dac_m_2.5mA': 0x32,
                          'cph_dac_c_2.5mA': 0x33,
                          'cph_dac_x1_25mA': 0x34,
                          'cph_dac_m_25mA': 0x35,
                          'cph_dac_c_25mA': 0x36,
                          'cph_dac_x1_ext_range_2': 0x37,
                          'cph_dac_m_ext_range_2': 0x38,
                          'cph_dac_c_ext_range_2': 0x39,
                          'cph_dac_x1_ext_range_1': 0x3a,
                          'cph_dac_m_ext_range_1': 0x3b,
                          'cph_dac_c_ext_range_1': 0x3c,
                          'dgs_dac': 0x3d,
                          'ramp_end_code': 0x3e,
                          'ramp_step_size': 0x3f,

                          'rclk_divider': 0x40,
                          'enable_ramp': 0x41,
                          'interrupt_ramp': 0x42,
                          'alarm_status': 0x43,
                          'alarm_status_and_clear': 0x44,
                          'cpl_dac_x1': 0x45,
                          'cpl_dac_m': 0x46,
                          'cpl_dac_c': 0x47,
                          'cph_dac_x1': 0x48,
                          'cph_dac_m': 0x49,
                          'cph_dac_c': 0x4a, }
