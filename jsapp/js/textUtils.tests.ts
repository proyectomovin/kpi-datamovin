import { afterEach, describe, expect, it } from '@jest/globals'
import envStore from '#/envStore'
import { replaceSupportEmail } from './textUtils'

const originalSupportEmail = envStore.data.support_email

afterEach(() => {
  envStore.data.support_email = originalSupportEmail
})

describe('replaceSupportEmail', () => {
  it('uses the support address configured by the deployment', () => {
    envStore.data.support_email = 'soporte@movin.com.ar'

    expect(replaceSupportEmail('Contact hola@movin.com.ar')).toBe('Contact soporte@movin.com.ar')
  })

  it('keeps the DataMovin fallback when no support address is configured', () => {
    envStore.data.support_email = ''

    expect(replaceSupportEmail('Contact hola@movin.com.ar')).toBe('Contact hola@movin.com.ar')
  })
})
